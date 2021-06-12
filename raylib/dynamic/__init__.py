"""
This is an attempt at a CFFI dynamic (ABI) binding.  It was failing in the exactly same place the ctypes binding fails, accessing
materials of a model.  But now it __seems__ to work
"""

import platform

# Probably unnecessary, just covering all bases in case people add or remove dlls
MAC_NAMES = ['libraylib.3.5.0.dylib', 'libraylib.301.dylib', 'libraylib.dylib']
LINUX_NAMES = ['libraylib.so.3.5.0','libraylib.so.3', 'libraylib.so']
WINDOWS_NAMES = ['libraylib.dll', 'raylib.dll','32bit/raylib.dll',  '32bit/libraylib.dll']

if platform.system() == "Darwin":
    NAMES_TO_TRY = MAC_NAMES
elif platform.system() == "Linux":
    NAMES_TO_TRY = LINUX_NAMES
elif platform.system() == "Windows":
    NAMES_TO_TRY = WINDOWS_NAMES
else:
    NAMES_TO_TRY = MAC_NAMES + LINUX_NAMES + WINDOWS_NAMES

import pathlib
MODULE = pathlib.Path(__file__).parent.parent

from cffi import FFI
ffi = FFI()
ffi.cdef(open(MODULE / "raylib_modified.h").read().replace('RLAPI ', ''))

for name in NAMES_TO_TRY:
    file = str(MODULE)+"/dynamic/"+name
    try:
        raylib = ffi.dlopen(file)
        print("LOADED DYNAMICALLY SHARED LIB "+file)
        break
    except Exception as e:
        print(e)

