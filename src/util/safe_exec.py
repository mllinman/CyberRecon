
import shutil, subprocess, threading
from typing import List, Optional, Callable

ALLOWLIST = {
    "nmap": ["nmap"],
    "tshark": ["tshark"],
    "snort": ["snort"],
    "python": ["python","python3"]
}

class SafeExecutor:
    def __init__(self, on_line: Optional[Callable[[str], None]] = None):
        self.on_line = on_line

    def run(self, tool: str, args: List[str]) -> int:
        if tool not in ALLOWLIST:
            raise RuntimeError(f"Tool '{tool}' is not allowlisted")
        exe = shutil.which(ALLOWLIST[tool][0])
        if not exe:
            if self.on_line: self.on_line(f"[warn] {tool} not found in PATH.")
            return 127
        cmd = [exe] + args
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        def pump():
            for line in proc.stdout:
                if self.on_line: self.on_line(line.rstrip())
        t = threading.Thread(target=pump, daemon=True); t.start()
        return proc.wait()