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
import re
import weakref
from array import array

from raylib import rl, ffi
from raylib.colors import *

try:
    from raylib.defines import *
except AttributeError:
    print("sorry deprecated enums dont work on dynamic version")

from inspect import getmembers, isbuiltin

current_module = __import__(__name__)


def _underscore(word: str) -> str:
    """
    from inflection
    """
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', word)
    word = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', word)
    word = word.replace("-", "_")
    return word.lower()


def pointer(struct):
    return ffi.addressof(struct)


# I'm concerned that we are doing a lot of string comparisons on every function call to detect types.
# Quickest way would probably be isinstance(result, ffi._backend._CDataBase) but that class name varies
# depending on if binding is static/dynamic
# (and possibly also different on pypy implementations?).
# which makes me reluctant to rely on it.
# Another possibility is ffi.typeof() but that will throw an exception if you give it a type that isn't a ctype
# Another way to improve performance might be to special-case simple types before doing the string comparisons

def _wrap_function(original_func):
    # print("makefunc ",a, ffi.typeof(a).args)
    def wrapped_func(*args):
        modified_args = []
        for (c_arg, arg) in zip(ffi.typeof(original_func).args, args):
            # print("arg:",str(arg), "c_arg.kind:", c_arg.kind, "c_arg:", c_arg, "type(arg):",str(type(arg)))
            if c_arg.kind == 'pointer':
                if type(arg) is str:
                    arg = arg.encode('utf-8')
                # if c_arg is a 'char *' not a 'const char *' then we ought to raise here because its an out
                # parameter and user should supply a ctype pointer, but cffi cant detect const
                # so we would have to get the info from raylib.json
                elif type(arg) is list and str(c_arg) == "<ctype 'char * *'>":
                    arg = [ffi.new("char[]", x.encode('utf-8')) for x in arg]
                elif is_cdata(arg) and "*" not in str(arg):
                    arg = ffi.addressof(arg)
                elif arg is None:
                    arg = ffi.NULL
                elif not is_cdata(arg):
                    if str(c_arg) == "<ctype '_Bool *'>":
                        raise TypeError(
                            "Argument must be a ctype bool, please create one with: pyray.ffi.new('bool *', True)")
                    elif str(c_arg) == "<ctype 'int *'>":
                        raise TypeError(
                            "Argument must be a ctype int, please create one with: pyray.ffi.new('int *', 1)")
                    elif str(c_arg) == "<ctype 'float *'>":
                        raise TypeError(
                            "Argument must be a ctype float, please create one with: pyray.ffi.new('float *', 1.0)")
            modified_args.append(arg)
        result = original_func(*modified_args)
        if result is None:
            return
        elif is_cdata(result) and str(result).startswith("<cdata 'char *'"):
            if str(result) == "<cdata 'char *' NULL>":
                return ""
            else:
                return ffi.string(result).decode('utf-8')
        else:
            return result

    # apparently pypy and cpython produce different types so check for both
    def is_cdata(arg):
        return str(type(arg)) == "<class '_cffi_backend.__CDataOwn'>" or str(
            type(arg)) == "<class '_cffi_backend._CDataBase'>"

    return wrapped_func


global_weakkeydict = weakref.WeakKeyDictionary()


def _make_struct_constructor_function(struct):
    def func(*args):
        # print(struct, args)
        modified_args = []
        for (field, arg) in zip(ffi.typeof(struct).fields, args):
            # print("arg:", str(arg), "field:", field[1], "field type:", field[1].type, "type(arg):", str(type(arg)))
            if arg is None:
                arg = ffi.NULL
            elif (field[1].type.kind == 'pointer'
                  and (str(type(arg)) == "<class 'numpy.ndarray'>"
                       or isinstance(arg, (array, bytes, bytearray, memoryview)))):
                arg = ffi.from_buffer(field[1].type, arg)
            modified_args.append(arg)
        s = ffi.new(f"struct {struct} *", modified_args)[0]
        global_weakkeydict[s] = modified_args
        return s

    return func


for name, attr in getmembers(rl):
    # print(name, attr)
    uname = _underscore(name).replace('3_d', '_3d').replace('2_d', '_2d')
    if isbuiltin(attr) or str(type(attr)) == "<class '_cffi_backend.__FFIFunctionWrapper'>" or str(
            type(attr)) == "<class '_cffi_backend._CDataBase'>":
        # print(attr.__call__)
        # print(attr.__doc__)
        # print(dir(attr))
        # print(dir(attr.__repr__))
        f = _wrap_function(attr)
        setattr(current_module, uname, f)
    else:
        setattr(current_module, name, attr)

for struct in ffi.list_types()[0]:
    f = _make_struct_constructor_function(struct)
    setattr(current_module, struct, f)

# overwrite ffi enums with our own
from raylib.enums import *
