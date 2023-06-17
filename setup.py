import sys
import os
from cx_Freeze import setup, Executable


files = ['icon.ico','themes/']
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

setup(
    name = "SafeMac",
    version = "1.0",
    description = "Construindo segurança, Proteção inteligente",
    author = "VoxarLabs",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)
