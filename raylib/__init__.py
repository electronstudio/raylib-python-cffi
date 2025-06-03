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
import logging

logger = logging.getLogger(__name__)

try:
    from ._raylib_cffi import ffi, lib as rl
except ModuleNotFoundError:
    logger.error("*** ERROR LOADING NATIVE CODE ***")
    logger.error("See https://github.com/electronstudio/raylib-python-cffi/issues/142")
    logger.error("Your Python is: %s", str(sys.implementation))
    raise

from raylib._raylib_cffi.lib import *
from raylib.colors import *
from raylib.defines import *
import cffi
from .version import  __version__

logger.warning("RAYLIB STATIC %s LOADED", __version__)
