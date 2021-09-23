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

from .static import rl, ffi
from .colors import *
from inspect import ismethod,getmembers,isbuiltin
import inflection

class PyRay:
    def pointer(self, struct):
        return ffi.addressof(struct)


def makefunc(a):
    #print("makefunc ",a, ffi.typeof(a).args)
    def func(self, *args):
        modified_args = []
        for (c_arg, arg) in zip(ffi.typeof(a).args, args):
            #print(arg, c_arg.kind)
            if type(arg) == str:
                encoded = arg.encode('utf-8')
                modified_args.append(encoded)
            elif c_arg.kind == 'pointer' and str(type(arg)) == "<class '_cffi_backend.__CDataOwn'>":
                modified_args.append(ffi.addressof(arg))
            else:
                modified_args.append(arg)
        return a(*modified_args)
    return func

def makeStructHelper(struct):
    def func(self, *args):
        return ffi.new(f"struct {struct} *", args)[0]
    return func


for name, attr in getmembers(rl):
    #print(name, attr)
    uname = inflection.underscore(name).replace('3_d','_3d').replace('2_d','_2d')
    if isbuiltin(attr) or str(type(attr)) == "<class '_cffi_backend.__FFIFunctionWrapper'>":
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

for struct in ffi.list_types()[0]:
    f = makeStructHelper(struct)
    setattr(PyRay, struct, f)

