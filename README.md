Python Bindings for Raylib

These bindings use CFFI rather than ctypes.  Hopefully this will be faster, the static type knowledge from the C
headers will result in fewer bugs, and using the original headers will make it easier to maintain.

Currently the goal is make usage as similar to the original C as CFFI will allow.  There are a few differences
you can see in the examples.  Making a 'Pythonic' library would be an additional layer on top which hasn't been
done yet.