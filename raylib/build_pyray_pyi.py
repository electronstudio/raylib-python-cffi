from .static import rl, ffi
from inspect import getmembers, isbuiltin
import inflection
import _cffi_backend
import re


def replace_types(text):
    text = re.sub('unsigned | \*|\* ', '', text)
    text = re.sub('unsigned', 'str', text)
    text = re.sub('char', 'str', text)
    text = re.sub('void', 'None', text)
    text = re.sub('long', 'int', text)
    text = re.sub('double', 'float', text)
    text = text.replace(' ', '_').replace('3_d', '_3d').replace('2_d', '_2d')
    return text


def build_to(filename):

    with open(filename, 'w') as f:
        f.write('class PyRay:\n')
        for name, attr in getmembers(rl):
            if name in ('TextFormat', 'TraceLog'):
                continue

            entry = '    '                          # base indent

            uname = inflection.underscore(name)
            uname = uname.replace('3_d', '_3d').replace('2_d', '_2d')

            is_wrapped = type(attr) == _cffi_backend.__FFIFunctionWrapper
            if isbuiltin(attr) or is_wrapped:
                entry += f'def {uname}(self'

                ctype = ffi.typeof(attr)
                for c, arg in enumerate(ctype.args):
                    arg_name = replace_types(arg.cname)
                    arg_name = inflection.underscore(arg_name)
                    arg_name += f'_{c}'

                    entry += f', {arg_name}'

                # close args and return type
                result = ctype.result.cname.split(' ')[0]
                result = replace_types(result)
                entry += f') -> {result} :\n'
                doc = ('\n' + ' '*8).join(attr.__doc__.split('\n'))
                entry += ' '*8 + f'"""{doc}"""\n'
                entry += ' '*8 + '...'
            else:
                entry += f'{name}: {type(attr).__name__}'

            f.write(f'{entry}\n')

        for struct in ('Vector2', 'Vector3', 'Vector4', 'Camera2D', 'Camera3D', 'Quaternion', 'Color', 'Rectangle'):
            entry = f'    {struct}: struct'
            f.write(f'{entry}\n')

        f.write(f'    class struct:\n')         # just to show struct on the others
        f.write(f'        ...\n')


if __name__ == '__main__':
    build_to('pyray.pyi')
