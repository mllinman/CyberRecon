# PyInstaller spec for CyberRecon Suite
from PyInstaller.utils.hooks import collect_submodules
a = Analysis(['main_launcher.py'],
             pathex=['.'],
             binaries=[],
             datas=[('assets', 'assets'), ('config', 'config'), ('CyberReconSuite_v1_4/docs', 'docs'), ('addons','addons'), ('src', 'src')],
             hiddenimports=collect_submodules('PyQt5'),
             hookspath=[],
             runtime_hooks=['build/pyi_rth_init.py'],
             excludes=[])
pyz = PYZ(a.pure, a.zipped_data, cipher=None)
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas,
          name='CyberReconSuite',
          console=False)
coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, name='CyberReconSuite_dist')
