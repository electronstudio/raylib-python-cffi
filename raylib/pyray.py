from .static import rl, ffi
from .colors import *
from inspect import ismethod,getmembers,isbuiltin
import inflection

class PyRay:
    def pointer(self, struct):
        return ffi.addressof(struct)


def makefunc(a):
    #print("makefunc ",a)
    def func(self, *args):
        modified_args = []
        for arg in args:
            #print(arg, type(arg))
            if type(arg) == str:
                encoded = arg.encode('utf-8')
                modified_args.append(encoded)
            else:
                modified_args.append(arg)
        return a(*modified_args)
    return func

def makeStructHelper(struct):
    def func(*args):
        return ffi.new(f"struct {struct} *", args)[0]
    return func


for name, attr in getmembers(rl):
    #print(name, attr)
    uname = inflection.underscore(name).replace('3_d','_3d').replace('2_d','_2d')
    if isbuiltin(attr):
        #print(attr.__call__)
        #print(attr.__doc__)
        #print(attr.__text_signature__)
        #print(dir(attr))
        #print(dir(attr.__repr__))
        f = makefunc(attr)
        setattr(PyRay, uname, f)
        #def wrap(*args):
        #    print("call to ",attr)
        #setattr(PyRay, uname, lambda *args: print("call to ",attr))
    else:
        setattr(PyRay, name, attr)

for struct in ('Vector2','Vector3','Vector4','Camera2D', 'Camera3D', 'Quaternion', 'Color'):
    f = makeStructHelper(struct)
    setattr(PyRay, struct, f)

