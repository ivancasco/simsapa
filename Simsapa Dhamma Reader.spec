# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=[],
    datas=[('simsapa/assets', 'simsapa/assets'), ('simsapa/alembic', 'simsapa/alembic'), ('simsapa/alembic.ini', 'simsapa/alembic.ini')],
    hiddenimports=['tiktoken_ext', 'tiktoken_ext.openai_public'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Simsapa Dhamma Reader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='arm64',
    codesign_identity=None,
    entitlements_file=None,
    icon=['simsapa/assets/icons/appicons/simsapa.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='Simsapa Dhamma Reader',
)
app = BUNDLE(
    coll,
    name='Simsapa Dhamma Reader.app',
    icon='simsapa/assets/icons/appicons/simsapa.ico',
    bundle_identifier='com.profound-labs.dhamma.simsapa',
)
