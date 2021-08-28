from raylib.static import rl, ffi

from inspect import ismethod, getmembers, isbuiltin
import inflection, sys

print("""from typing import Any

class struct: ...

""")


def ctype_to_python_type(t):
    if t == '_Bool':
        return "bool"
    elif t == 'void':
        return 'None'
    elif t == "long":
        return "int"
    elif t == "double":
        return "float"
    elif "char *" in t:
        return "str"
    elif "char" in t:
        return "str"  # not sure about this one
    elif "*" in t:
        return "Any"
    elif t.startswith("struct"):
        return t.replace("struct ","")
    elif t.startswith("unsigned"):
        return t.replace("unsigned ", "")
    else:
        return t


for name, attr in getmembers(rl):
    uname = name
    if isbuiltin(attr) or str(type(attr)) == "<class '_cffi_backend.__FFIFunctionWrapper'>":

        sig = ""
        for i, arg in enumerate(ffi.typeof(attr).args):
            param_name = arg.cname.replace("struct", "").replace("char *", "str").replace("*",
                                                                                          "_pointer").replace(
                " ", "")
            param_type = ctype_to_python_type(arg.cname)
            sig += f"{param_name}_{i}: {param_type},"

        return_type = ffi.typeof(attr).result.cname

        print(
            f'def {uname}({sig}) -> {ctype_to_python_type(return_type)}:\n        """{attr.__doc__}"""\n        ...')

    elif str(type(attr)) == "<class '_cffi_backend._CDataBase'>":
        return_type = ffi.typeof(attr).result.cname
        print(
            f'def {uname}(*args) -> {ctype_to_python_type(return_type)}:\n        """VARARG FUNCTION - MAY NOT BE SUPPORTED BY CFFI"""\n        ...')
    else:
        #print("*****", str(type(attr)))
        print(f"{name}: {str(type(attr))[8:-2]}")  # this isolates the type

for struct in ffi.list_types()[0]:
    print("processing", struct, file=sys.stderr)
    if ffi.typeof(struct).kind == "struct":
        # if ffi.typeof(struct).fields is None:
        #     print("weird empty struct, skipping", file=sys.stderr)
        #     break
        print(f"{struct}: struct")
        # sig = ""
        # for arg in ffi.typeof(struct).fields:
        #     sig += ", " + arg[0]
        # print(f"        def __init__(self{sig}):")
        #
        # for arg in ffi.typeof(struct).fields:
        #     print(f"            self.{arg[0]}={arg[0]}")

    elif ffi.typeof(struct).kind == "enum":
        print(f"{struct}: int")
    else:
        print("ERROR UNKNOWN TYPE", ffi.typeof(struct), file=sys.stderr)


