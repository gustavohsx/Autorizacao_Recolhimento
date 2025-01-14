import sys
from cx_Freeze import setup, Executable

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="AutorizacaoRecolhimento",
    version="2.0",
    description="Programa Gerador de Altorização de Recolhimento",
    executables=[Executable("main.py", base=base)],
    
)