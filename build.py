import PyInstaller.__main__
import os
import sys

# Use correct path separator for OS
separator = ';' if sys.platform == 'win32' else ':'

PyInstaller.__main__.run([
    'run_gui.py',
    '--name=MockAPIServer',
    '--onefile',
    f'--add-data=app/templates{separator}app/templates',
    '--hidden-import=flask',
    '--hidden-import=flask_sqlalchemy',
    '--hidden-import=sqlalchemy',
    '--noconfirm',
    '--clean'
])