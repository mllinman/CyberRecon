import importlib.util, inspect, os, sys
from typing import List, Tuple, Optional, Type

# Contract: an add-on file must expose either:
#   - a QWidget subclass named `Addon`, or
#   - a function `get_addon()` that returns (widget_class, label_str)
#
# Example:
#   class Addon(QWidget): ...
#   LABEL = "My Addon"  # optional, else class name is used
#
# OR
#   def get_addon(): return (MyWidgetClass, "My Addon")

def _load_module_from_path(py_path: str):
    mod_name = f"addon_{os.path.splitext(os.path.basename(py_path))[0]}"
    spec = importlib.util.spec_from_file_location(mod_name, py_path)
    if not spec or not spec.loader:
        return None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = mod
    spec.loader.exec_module(mod)
    return mod

def discover_addons(addons_dir: str) -> List[Tuple[Type, str]]:
    """Return list of (widget_class, label)."""
    results: List[Tuple[Type, str]] = []
    if not os.path.isdir(addons_dir):
        return results

    for name in sorted(os.listdir(addons_dir)):
        if not name.endswith(".py") or name.startswith("_"):
            continue
        path = os.path.join(addons_dir, name)
        try:
            mod = _load_module_from_path(path)
            if mod is None:
                continue
            # 1) get_addon() contract
            if hasattr(mod, "get_addon"):
                widget_cls, label = mod.get_addon()
                results.append((widget_cls, str(label)))
                continue
            # 2) class Addon(QWidget) contract
            if hasattr(mod, "Addon"):
                from PyQt5.QtWidgets import QWidget
                cls = getattr(mod, "Addon")
                if inspect.isclass(cls) and issubclass(cls, QWidget):
                    label = getattr(mod, "LABEL", cls.__name__)
                    results.append((cls, str(label)))
        except Exception as e:
            # don’t crash the app if an add-on is broken
            print(f"[addon loader] failed to load {name}: {e}")
            continue
    return results