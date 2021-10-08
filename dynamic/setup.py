import pathlib
from setuptools import setup
from setuptools.dist import Distribution
from version import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.rst").read_text()


# This call to setup() does all the work
setup(
    name="raylib_dynamic",
    version=__version__,
    description="Python CFFI bindings for Raylib DLL version",
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/electronstudio/raylib-python-cffi",
    author="Electron Studio",
    author_email="github@electronstudio.co.uk",
    license="EPL-2.0",
    classifiers=[
        "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["raylib", "pyray"],
    include_package_data=True,
    install_requires=["cffi>=1.14.5","inflection"],
)


