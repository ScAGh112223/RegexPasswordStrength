from sys import platform


import platform, subprocess, importlib
import re, os

__all__ = ["re", "os"]

match platform.system():
    case "Linux":
        subprocess.check_call([sys.executable, "-m", "pip", "install", "getch"],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)
        getch = importlib.import_module("getch").getch
        __all__.append("getch")
    case "Windows":
        getch = importlib.import_module("msvcrt").getch
        __all__.append("getch")