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
import inflection, sys, json, re

two_or = re.compile(r'''\(\s*([^\s]*)\s*\|\s*([^\s]*)\s*\)''')
three_or = re.compile(r'''\(\s*([^\s]*)\s*\|\s*([^\s]*)\s*\|\s*(^\s*)\s*\)''')
two_mult = re.compile(r'''\(\s*([^\s]*)\s*\*\s*([^\s]*)\s*\)''')
two_div = re.compile(r'''\(\s*([^\s]*)\s*/\s*([^\s]*)\s*\)''')

def process(filename):
    f = open(filename, "r")
    js = json.load(f)
    known_define = []
    known_enum = []
    for e in js['enums']:
        if e['name'] and e['values']:
            for v in e['values']:
                if v['name']:
                    known_enum.append(str(v['name']).strip())
    for e in js['defines']:
        if e['type'] in ('INT', 'FLOAT', 'STRING'):
            if e['type'] == 'INT':
                print(e['name'] + ": int = " + str(e['value']).strip())
            elif e['type'] == 'FLOAT':
                print(e['name'] + ": float = " + str(e['value']).strip())
            else:
                print(e['name'] + ": str = \"" + str(e['value']).strip() + '"')
            known_define.append(str(e['name']).strip())
        elif e['type'] == "UNKNOWN":
            strval = str(e['value']).strip()
            if strval.startswith("__"):
                continue
            # if strval in known_enum:
            #     print(e['name'] + " = raylib." + strval)
            elif strval in known_define:
                print(e['name'] + " = " + strval)
            else:
                matches = two_or.match(strval)
                if not matches:
                    matches = three_or.match(strval)
                if matches:
                    match_defs = [str(m).strip() for m in matches.groups()]
                    if all(d in known_enum for d in match_defs):
                        print(e['name'] + " = " + " | ".join(("raylib."+m) for m in match_defs))
                    elif all(d in known_define for d in match_defs):
                        print(e['name'] + " = " + " | ".join(match_defs))
                else:
                    continue
            known_define.append(str(e['name']).strip())
        elif e['type'] == "FLOAT_MATH":
            strval = str(e['value']).strip()
            matches = two_mult.match(strval)
            if matches:
                match_defs = [str(m).strip() for m in matches.groups()]
                match_parts = []
                for m in match_defs:
                    if "." in m:
                        match_parts.append(m.rstrip("f"))
                    else:
                        match_parts.append(m)
                if all(d in known_enum for d in match_parts):
                    print(e['name'] + " = " + " * ".join(("raylib." + m) for m in match_parts))
                elif all(d in known_define for d in match_parts):
                    print(e['name'] + " = " + " * ".join(match_parts))
            else:
                matches = two_div.match(strval)
                if matches:
                    match_defs = [str(m).strip() for m in matches.groups()]
                    match_parts = []
                    for m in match_defs:
                        if "." in m:
                            match_parts.append(m.rstrip("f"))
                        else:
                            match_parts.append(m)
                    if any(d in known_enum for d in match_parts):
                        print(e['name'] + " = " + " / ".join(("raylib." + m) for m in match_parts))
                    elif any(d in known_define for d in match_parts):
                        print(e['name'] + " = " + " / ".join(match_parts))
                else:
                    continue

print("import raylib\n")

process("raylib.json")
process("raymath.json")
process("rlgl.json")
process("raygui.json")
process("physac.json")
process("glfw3.json")

