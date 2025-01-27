# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('src\\\\data\\\\enml.tsv', 'src/data'), ('src\\\\data\\\\datuk.tsv', 'src/data'), ('src\\\\assets\\\\ma.ico', 'src/assets'), ('src\\\\assets\\\\Manjari-Regular.ttf', 'src/assets'), ('src\\\\assets\\\\light_styles.qss', 'src/assets'), ('src\\\\assets\\\\dark_styles.qss', 'src/assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Mazha',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['src\\assets\\ma.ico'],
)
