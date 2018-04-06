# -*- mode: python -*-

block_cipher = None


a = Analysis(['Snapcon Fortnite v2.0.0.py'],
             pathex=['C:\\Users\\Eivind\\Desktop\\Fortnite\\Fortnite-Snapcon-2.0'],
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
          name='Snapcon Fortnite v2.0.0',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='icon.ico')
