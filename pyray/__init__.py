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
    word = re.sub('2D$', '_2d', word)
    word = re.sub('3D$', '_3d', word)
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', word)
    word = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', word)
    word = word.replace("-", "_")
    return word.lower()


def _wrap_function(original_func):
    c_args = [str(x) for x in ffi.typeof(original_func).args]
    number_of_args = len(c_args)
    c_arg_is_pointer = [x.kind == 'pointer' for x in ffi.typeof(original_func).args]
    c_arg_is_string = [str(x) == "<ctype 'char *'>" for x in ffi.typeof(original_func).args]
    # c_arg_is_void_pointer = [str(x) == "<ctype 'void *'>" for x in ffi.typeof(original_func).args]

    def wrapped_func(*args):
        args = list(args)  # tuple is immutable, converting it to mutable list is faster than constructing new list!
        for i in range(number_of_args):
            try:
                arg = args[i]
            except IndexError:
                raise RuntimeError(f"function requires {number_of_args} arguments but you supplied {len(args)}")
            if c_arg_is_pointer[i]:
                if c_arg_is_string[i]:  # we assume c_arg is 'const char *'
                    try:  # if it's a non-const 'char *' then user should be supplying a ctype pointer, not a Python
                        # string
                        args[i] = arg.encode('utf-8')  # in that case this conversion will fail
                    except AttributeError:  # but those functions are uncommon, so quicker on average to try the
                        # conversion
                        pass  # and ignore the exception
                # if user supplied a Python string but c_arg is a 'char *' not a 'const char *' then we ought to raise
                # exception because its an out
                # parameter and user should supply a ctype pointer, but we cant because cffi cant detect 'const'
                # so we would have to get the info from raylib.json
                elif c_args[i] == "<ctype 'char * *'>" and type(arg) is list:
                    args[i] = [ffi.new("char[]", x.encode('utf-8')) for x in arg]
                elif is_cdata(arg) and "*" not in str(arg):
                    args[i] = ffi.addressof(arg)
                elif arg is None:
                    args[i] = ffi.NULL
                elif not is_cdata(arg):
                    if c_args[i] == "<ctype '_Bool *'>":
                        raise TypeError(
                            f"Argument {i} ({arg}) must be a ctype bool, please create one with: pyray.ffi.new('bool "
                            f"*', True)")
                    elif c_args[i] == "<ctype 'int *'>":
                        raise TypeError(
                            f"Argument {i} ({arg}) must be a ctype int, please create one with: pyray.ffi.new('int "
                            f"*', 1)")
                    elif c_args[i] == "<ctype 'float *'>":
                        raise TypeError(
                            f"Argument {i} ({arg}) must be a ctype float, please create one with: pyray.ffi.new("
                            f"'float *', 1.0)")
                    elif c_args[i] == "<ctype 'void *'>":
                        # we could assume it's a string and try to convert it but we would have to be sure it's
                        # const.  that seems reasonable assumption for char* but i'm not confident it is for void*
                        raise TypeError(
                            f"Argument {i} ({arg}) must be a cdata pointer. Type is void so I don't know what type it "
                            f"should be."
                            "If it's a const string you can create it with pyray.ffi.new('char []', b\"whatever\") . "
                            "If it's a float you can create it with pyray.ffi.new('float *', 1.0)")

        result = original_func(*args)
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
        s = ffi.new(f"{struct} *", modified_args)[0]
        global_weakkeydict[s] = modified_args
        return s

    return func


for name, attr in getmembers(rl):
    # print(name, attr)
    uname = _underscore(name)
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


def text_format(*args):
    raise RuntimeError("Use Python f-strings etc rather than calling text_format().")
