import pathlib
from setuptools import setup
from setuptools.dist import Distribution


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
VERSION = (HERE / "version.py").read_text().split()[-1].strip("\"'")


class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(foo):
        return True

# This call to setup() does all the work
setup(
    name="raylib_sdl",
    version=VERSION,
    description="Python CFFI bindings for Raylib",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/electronstudio/raylib-python-cffi",
    author="Electron Studio",
    author_email="github@electronstudio.co.uk",
    license="EPL-2.0",
    classifiers=[
        "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["raylib", "pyray"],
    include_package_data=True,
    setup_requires=["cffi>=1.17.1"],
    install_requires=["cffi>=1.17.1"],
    distclass=BinaryDistribution,
    cffi_modules=["raylib/build.py:ffibuilder"]
)
