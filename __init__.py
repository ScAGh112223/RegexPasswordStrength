import sys, platform, subprocess, importlib, os # Packages either only required in __init__ or interfaced through __init__
import re # regex

__all__ = ["re"] # Initialize __all__ with regex

# Ensuring that the program works in both linux-based OS's and Windows(haven't considered MacOS)
match platform.system():
    case "Linux": # If the OS is Linux
        # Install the "getch" package required for live input
        subprocess.check_call([sys.executable, "-m", "pip", "install", "getch"],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)
        getch = importlib.import_module("getch").getch # Import getch function so that it can be used directly
        decode = lambda i: i # Dummy function to keep main.py (dummy because getch doesn't return bytes)
        clear_screen = lambda: os.system("clear") # Different commands for windows and linux
        to_byteStr = lambda i: bytes(i, "utf-8") # To byte string so that enter key and backspace key can be detectes
        
        backspace_code = b"\x7f" # Normal string to byte string version of backspace
        enter_code = b"\n" # Just newline in byte form

        __all__.extend(["getch", "clear_screen", "decode", "to_byteStr", "backspace_code", "enter_code"]) # Add all variables to __all__
    case "Windows":
        getch = importlib.import_module("msvcrt").getch # Import msvcrt.getch (getch for windows) directly as it doesn't need to be installed
        decode = lambda i: i.decode("utf-8") # Actual decode function(contaray to linux decode) as msvcrt getch returns byte strings
        clear_screen = lambda: os.system("cls") # Clearn screen command for windows
        to_byteStr = lambda i: i # Dummy to byte string function as msvcrt.getch already returns bytes

        backspace_code = b"\r" # Return carriage(backspace) in bytes
        enter_code = b"\x08" # Byte code for enter

        __all__.extend(["getch", "clear_screen", "decode", "to_byteStr", "backspace_code", "enter_code"]) # Add all variables to __all__
