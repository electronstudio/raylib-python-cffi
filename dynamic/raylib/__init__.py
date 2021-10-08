"""
This is an attempt at a CFFI dynamic (ABI) binding.  It was failing in the exactly same place the ctypes binding fails, accessing
materials of a model.  But now it __seems__ to work
"""

#  Copyright (c) 2021 Richard Smith and others
#
#  This program and the accompanying materials are made available under the
#  terms of the Eclipse Public License 2.0 which is available at
#  http://www.eclipse.org/legal/epl-2.0.
#
#  This Source Code may also be made available under the following Secondary
#  licenses when the conditions for such availability set forth in the Eclipse
#  Public License, v. 2.0 are satisfied: GNU General Public License, version 2
#  with the GNU Classpath Exception which is
#  available at https://www.gnu.org/software/classpath/license.html.
#
#  SPDX-License-Identifier: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0

from cffi import FFI
import itertools
import os
import pathlib
import platform
from .version import __version__


MODULE = pathlib.Path(__file__).parent

def raylib_library_path():
    '''Return the full path of the raylib shared library
    If the environment variable "USE_EXTERNAL_RAYLIB" is set (no value required)
    then the library will be loaded from the system library paths.
    '''
    def so_path():
        return str(MODULE) if not 'USE_EXTERNAL_RAYLIB' in os.environ else ''
    def so_name():
        '''Returns the appropriate for the library on the current platform.'''
        lib_filenames = {
            'Windows': 'libraylib.dll',
            'Linux': 'libraylib.so',
            'Darwin': 'libraylib.dylib',
        }
        if platform.system() not in lib_filenames:
            raise ValueError('Unrecognised system "{}"'.format(platform.system()))
        return lib_filenames.get(platform.system())

    return os.path.join(so_path(), so_name())


ffi = FFI()
ffi.cdef(open(MODULE / "raylib_modified.h").read().replace('RLAPI ', ''))

try:
    raylib_fname = raylib_library_path()
    rl = ffi.dlopen(raylib_fname)
    print('LOADED DYNAMICALLY SHARED LIB {} {}'.format(__version__, raylib_fname))
except Exception as e:
    print(e)

LIGHTGRAY  =( 200, 200, 200, 255 )
GRAY       =( 130, 130, 130, 255 )
DARKGRAY   =( 80, 80, 80, 255 )
YELLOW     =( 253, 249, 0, 255 )
GOLD       =( 255, 203, 0, 255 )
ORANGE     =( 255, 161, 0, 255 )
PINK       =( 255, 109, 194, 255 )
RED        =( 230, 41, 55, 255 )
MAROON     =( 190, 33, 55, 255 )
GREEN      =( 0, 228, 48, 255 )
LIME       =( 0, 158, 47, 255 )
DARKGREEN  =( 0, 117, 44, 255 )
SKYBLUE    =( 102, 191, 255, 255 )
BLUE       =( 0, 121, 241, 255 )
DARKBLUE   =( 0, 82, 172, 255 )
PURPLE     =( 200, 122, 255, 255 )
VIOLET     =( 135, 60, 190, 255 )
DARKPURPLE =( 112, 31, 126, 255 )
BEIGE      =( 211, 176, 131, 255 )
BROWN      =( 127, 106, 79, 255 )
DARKBROWN  =( 76, 63, 47, 255 )
WHITE      =( 255, 255, 255, 255 )
BLACK      =( 0, 0, 0, 255 )
BLANK      =( 0, 0, 0, 0 )
MAGENTA    =( 255, 0, 255, 255 )
RAYWHITE   =( 245, 245, 245, 255 )