# -*- mode: python -*-

block_cipher = None


a = Analysis(['ui_main.py'],
             pathex=['.\\icon', 'E:\\02_Task\\01_PD_Analyzer\\PD_Analyzer\\PD_Analyzer'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ui_main',
          debug=False,
          strip=False,
          upx=True,
          console=False )
