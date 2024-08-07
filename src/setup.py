from cx_Freeze import setup, Executable
import sys, os

sys.path.append(os.path.abspath("./utils/"))
sys.path.append(os.path.abspath("./interfaces/"))

base = None

if sys.platform == "win32":
    base = "Win32Gui"


executables = [
    Executable("SpotiLike.py", base=base, icon="icon.ico", shortcut_name="SpotiLike <3")
]

packages = [
    "idna",
    "PyQt5.QtWidgets",
    "PyQt5.uic",
    "PyQt5.QtCore",
    "PyQt5.QtGui",
    "pynput",
    "logging",
    "sys",
    "traceback",
    "spotipy",
    "os",
    "fuzzywuzzy",
    "string",
    "ctypes",
    "urllib.request",
    "pynput.keyboard._xorg",
    "pynput.mouse._xorg",
]
options = {
    "build_exe": {
        "packages": packages,
        "include_files": [
            "uis",
            "icon.ico",
            "assets",
            "config",
        ],
        "zip_include_packages": "PyQt5",
        "includes": [
            "PyQt5.QtCore",
            "PyQt5.QtGui",
            "PyQt5.QtWidgets",
            "format_hotkey",
            "thread",
            "playlists",
            "main",
            "settings",
            "error_handler",
        ],
        "excludes": ["tkinter", "PySide2"],
    },
}

setup(
    name="SpotiLike <3",
    options=options,
    version=2.1,
    description="SpotiLike🔔💕",
    executables=executables,
)
