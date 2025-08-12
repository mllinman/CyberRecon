# PyInstaller spec for CyberRecon Suite
from PyInstaller.utils.hooks import collect_submodules
a = Analysis(['src/main.py'],
             pathex=['.'],
             binaries=[],
             datas=[('assets', 'assets'), ('config', 'config'), ('docs', 'docs'),('addons','addons')],
             hiddenimports=collect_submodules('PyQt5'),
             hookspath=[],
             runtime_hooks=[],
             excludes=[])
pyz = PYZ(a.pure, a.zipped_data, cipher=None)
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas,
          name='CyberReconSuite',
          console=False)
coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, name='CyberReconSuite_dist')
