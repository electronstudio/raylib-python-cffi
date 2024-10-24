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

import sys
try:
    from ._raylib_cffi import ffi, lib as rl
except ModuleNotFoundError:
    print("\n*** ERROR LOADING NATIVE CODE ***\n")
    print("See https://github.com/electronstudio/raylib-python-cffi/issues/142\n", file=sys.stderr)
    print("Your Python is: "+str(sys.implementation)+"\n", file=sys.stderr)
    raise
from raylib._raylib_cffi.lib import *
from raylib.colors import *
from raylib.defines import *
import cffi
from .version import  __version__

print("RAYLIB STATIC "+__version__+" LOADED", file=sys.stderr)

