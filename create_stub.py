from raylib.static import rl, ffi

from inspect import ismethod,getmembers,isbuiltin
import inflection


print("""from typing import Any

class PyRay:
    def pointer(self, struct):
        return ffi.addressof(struct)
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
    elif "*" in t:
        return "Any"
    elif t.startswith("struct"):
        return "Any" # This should be CData but cant get PyCharm to understand that - it just shows up as None
    elif t.startswith("unsigned"):
        return t.replace("unsigned ","")
    else:
        return t

for name, attr in getmembers(rl):
    uname = inflection.underscore(name).replace('3_d', '_3d').replace('2_d', '_2d')
    if isbuiltin(attr) or str(type(attr)) == "<class '_cffi_backend.__FFIFunctionWrapper'>":


        sig = ""
        for i, arg in enumerate(ffi.typeof(attr).args):
            param_name = arg.cname.replace("struct","").replace("char *","str").replace("*","_pointer").replace(" ","")
            param_type = ctype_to_python_type(arg.cname)
            sig += f", {param_name}_{i}: {param_type}"


        return_type = ffi.typeof(attr).result.cname


        print(f"    def {uname}(self{sig}) -> {ctype_to_python_type(return_type)}: ...")


    else:
        print(f"    {name}: {str(type(attr))[8:-2]}")           # this isolates the type


for struct in ffi.list_types()[0]:
    print(f"    {struct}: Any") # This should be CData but cant get PyCharm to understand that - it just shows up as None
