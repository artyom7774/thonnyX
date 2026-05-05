"""
pyinstaller -F -w --icon="thonny.ico" Thonny.py
.venv/Scripts/pyinstaller.exe -F -w  --icon="thonny.ico" --hidden-import=requests Thonny.py

"""

from thonny.__main__ import *
