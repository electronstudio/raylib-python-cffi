# Python Bindings for Raylib

This uses CFFI API static bindins rather than ctypes.  Hopefully this will be faster, the static type knowledge from the C
headers will result in fewer bugs, and using the original headers will make it easier to maintain.

Currently the goal is make usage as similar to the original C as CFFI will allow.  There are a few differences
you can see in the examples.  Making a 'Pythonic' library would be an additional layer on top which hasn't been
done yet.

See test.py and examples/*.py for how to use.

# Platforms tested

 * MacOS 10.12.6

# HELP WANTED

 * converting more examples from C to python
 * testing and building on more platforms
 
### Dynamic bindings

I have attempted to do CFFI ABI dynamic bindings too in order to avoid the need to compile a C extension module,
but they don't work properly.  They fails to work in the same place the ctypes binding fails, accessing
materials of a model, because Python can't dynamically tell the difference between a pointer and an array. There's probably
  some way to specify this (e.g. in raylib_modified.h) but it's difficult to be sure we fixed them all, and the errors
 are often completely silent.
 
 See test_static.py for the non-working example.