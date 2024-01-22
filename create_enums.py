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

from raylib import rl, ffi

from inspect import ismethod, getmembers, isbuiltin
import inflection, sys, json

def process(filename):
    f = open(filename, "r")
    js = json.load(f)

    for e in js['enums']:
        if e['name'] and e['values']:
            print ("class "+e['name']+"("+"IntEnum):")
            for value in e['values']:
                print("    "+value['name']+" = "+str(value['value']))
            print("")

print("""from enum import IntEnum
""")

process("raylib.json")
process("raygui.json")
process("glfw3.json")
