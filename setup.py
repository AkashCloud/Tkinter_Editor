import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

build_exe_options = {"packages": ["os", "tkinter"], "include_files":["E:/tkinter proj2/icon/icon.ico"]}
executables = [cx_Freeze.Executable("WorkPad.py", base=base, icon ="E:/tkinter proj2/icon/icon.ico")]

cx_Freeze.setup(  name = "guifoo",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables =executables
        
        )