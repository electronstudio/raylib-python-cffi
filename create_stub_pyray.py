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

from pathlib import Path
from raylib import rl, ffi
from pyray import _underscore
from inspect import ismethod, getmembers, isbuiltin
import inflection, sys, json

known_functions = {}
known_structs = {}
for filename in (Path("raylib.json"), Path("raymath.json"), Path("rlgl.json"), Path("raygui.json"), Path("physac.json"),
                 Path("glfw3.json")):
    f = open(filename, "r")
    js = json.load(f)
    for fn in js["functions"]:
        if fn["name"] not in known_functions:
            known_functions[fn["name"]] = fn
    for st in js["structs"]:
        if st["name"] not in known_structs:
            known_structs[st["name"]] = st
    for e in js['enums']:
        if e['name'] and e['values']:
            print ("class "+e['name']+"(int):")
            for value in e['values']:
                print("    "+value['name']+" = "+str(value['value']))
            print("")


def ctype_to_python_type(t):
    if t == '_Bool':
        return "bool"
    elif t == 'void':
        return 'None'
    elif t == "long":
        return "int"
    elif t == "unsigned long long":
        return "int"
    elif t == "uint64_t":
        return "int"
    elif t == "short":
        return "int"
    elif t == "unsigned short":
        return "int"
    elif t == "double":
        return "float"
    elif "char * *" in t:
        return "list[str]"
    elif "char *" in t:
        return "str"
    elif t == "char":
        return "str"  # not sure about this one
    elif t == "unsigned char":
        return "int"
    elif "*" in t:
        return "Any"
    elif "[" in t:
        return "list" # TODO FIXME type of items in the list
    elif t.startswith("struct"):
        return t.replace("struct ", "")
    elif t.startswith("unsigned"):
        return t.replace("unsigned ", "")
    elif t.startswith("enum"):
        return t.replace("enum ", "")
    else:
        return t


print("""from typing import Any

import _cffi_backend # type: ignore

ffi: _cffi_backend.FFI
""")

# These words can be used for c arg names, but not in python
reserved_words = ("in", "list", "tuple", "set", "dict", "from", "range", "min", "max", "any", "all", "len")

for name, attr in getmembers(rl):
    uname = _underscore(name)
    if isbuiltin(attr) or str(type(attr)) == "<class '_cffi_backend.__FFIFunctionWrapper'>":
        json_object = known_functions.get(name, None)
        if json_object is None:
            # this is _not_ an exported function from raylib, raymath, rlgl raygui or physac
            # so we don't want it in the pyray API
            continue
        sig = ""
        for i, arg in enumerate(ffi.typeof(attr).args):
            param_name = arg.cname.replace("struct", "").replace("char *", "str").replace("*",
                                                                                          "_pointer").replace(
                " ", "") + "_" + str(i)
            if 'params' in json_object:
                p = json_object['params']
                param_name = list(p)[i]['name']
                # don't use a python reserved word:
                if param_name in reserved_words:
                    param_name = param_name + "_" + str(i)
            param_type = ctype_to_python_type(arg.cname)
            if "struct" in arg.cname:
                param_type += "|list|tuple"
            sig += f"{param_name}: {param_type},"

        return_type = ffi.typeof(attr).result.cname

        description = attr.__doc__

        if 'description' in json_object:
            description = json_object['description']

        print(
            f'def {uname}({sig}) -> {ctype_to_python_type(return_type)}:\n        """{description}"""\n        ...')

    elif str(type(attr)) == "<class '_cffi_backend._CDataBase'>":
        return_type = ffi.typeof(attr).result.cname
        print(
            f'def {uname}(*args) -> {ctype_to_python_type(return_type)}:\n        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""\n        ...')
    else:
        # print("*****", str(type(attr)))
        t = str(type(attr))[8:-2]  # this isolates the type
        if t != "int":
            print(f"{name}: {t}")

for struct in ffi.list_types()[0]:
    print("processing", struct, file=sys.stderr)

    if ffi.typeof(struct).kind == "struct":
        json_object = known_structs.get(struct, None)
        if json_object is None:
            # this is _not_ an exported struct from raylib, raymath, rlgl raygui or physac
            # so we don't want it in the pyray API
            continue
        if ffi.typeof(struct).fields is None:
            print("weird empty struct, skipping " + struct, file=sys.stderr)
            continue
        print(f"class {struct}:")
        print(f'    """ struct """')
        sig = ""
        for arg in ffi.typeof(struct).fields:
            ptype = ctype_to_python_type(arg[1].type.cname)
            if arg[1].type.kind == "struct":
                ptype += "|list|tuple"
            sig += f", {arg[0]}: {ptype}|None = None"
        print(f"    def __init__(self{sig}):")

        for arg in ffi.typeof(struct).fields:
            print(f"        self.{arg[0]}:{ctype_to_python_type(arg[1].type.cname)} = {arg[0]} # type: ignore")

    # elif ffi.typeof(struct).kind == "enum":
    #    print(f"{struct}: int")
    else:
        print("WARNING: SKIPPING UNKNOWN TYPE", ffi.typeof(struct), file=sys.stderr)

print("""
LIGHTGRAY  : Color
GRAY       : Color
DARKGRAY   : Color
YELLOW     : Color
GOLD       : Color
ORANGE     : Color
PINK       : Color
RED        : Color
MAROON     : Color
GREEN      : Color
LIME       : Color
DARKGREEN  : Color
SKYBLUE    : Color
BLUE       : Color
DARKBLUE   : Color
PURPLE     : Color
VIOLET     : Color
DARKPURPLE : Color
BEIGE      : Color
BROWN      : Color
DARKBROWN  : Color
WHITE      : Color
BLACK      : Color
BLANK      : Color
MAGENTA    : Color
RAYWHITE   : Color
""")
