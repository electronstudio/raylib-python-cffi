import pathlib
from setuptools import setup
from setuptools.dist import Distribution
import os

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
VERSION = (HERE / "version.py").read_text().split()[-1].strip("\"'")

RAYLIB_PLATFORM = os.getenv("RAYLIB_PLATFORM", "Desktop")
if RAYLIB_PLATFORM == "SDL":
    NAME = "_sdl"
elif RAYLIB_PLATFORM == "DRM":
    NAME = "_drm"
else:
    NAME = ""

class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(foo):
        return True

# should be name="raylib"+NAME but then Github doesn't track dependants
setup(
    name="raylib"+NAME,
    version=VERSION,
    description="Python CFFI bindings for Raylib",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/electronstudio/raylib-python-cffi",
    author="Electron Studio",
    author_email="github@electronstudio.co.uk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["raylib", "pyray"],
    include_package_data=True,
    install_requires=["cffi>=1.17.1"],
    distclass=BinaryDistribution,
    cffi_modules=["raylib/build.py:ffibuilder"]
)
