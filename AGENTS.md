# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is raylib-python-cffi8, Python CFFI bindings for Raylib 5.5 game development library. It provides two main Python modules:
- `raylib`: Direct C API bindings (exact copy of C functions)  
- `pyray`: More Pythonic API wrapper

## Key Architecture

- `/raylib/`: Core static CFFI bindings module with build system
- `/pyray/`: Pythonic wrapper API module
- `/dynamic/`: Dynamic binding version (separate package)
- `/examples/`: Python example code organized by category (core, audio, textures, etc.)
- `/raylib-c/`: Embedded Raylib C library source (git submodule)
- `/raygui/`: Embedded raygui C library source (git submodule)  
- `/physac/`: Embedded physac physics library source
- `/tests/`: Test scripts for both static and dynamic versions

## Build System

The project uses CFFI with setuptools. Main build entry point is `raylib/build.py` which:
- Parses C headers from embedded libraries
- Generates CFFI bindings
- Handles platform-specific linking (Desktop/SDL/DRM backends)
- Supports environment variable customization for build paths

## Development Commands

### Building from source
```bash
# Build Python library manually
python3 raylib/build.py

# Build wheel distribution  
pip3 install wheel
python3 setup.py bdist_wheel

# Install from wheel
pip3 install dist/raylib*.whl
```

### Testing
```bash
# Run main test suite
cd tests && ./run_tests.sh

# Run dynamic version tests  
cd tests && ./run_tests_dynamic.sh

# Individual test files can be run with python3
python3 tests/test_hello_world.py
```

### Multiple platform builds
```bash
# Build for multiple Python versions (Linux)
./raylib/build_multi_linux.sh

# Build for multiple Python versions (general)
./raylib/build_multi.sh
```

### Documentation
```bash
# Generate docs (uses Sphinx)
./make_docs.sh
```

## Environment Variables for Build Customization

- `RAYLIB_PLATFORM`: Desktop (default), SDL, DRM, PLATFORM_COMMA
- `RAYLIB_LINK_ARGS`: Manual linker arguments instead of pkg-config
- `RAYLIB_INCLUDE_PATH`: Custom path to raylib.h
- `RAYGUI_INCLUDE_PATH`: Custom path to raygui.h  
- `GLFW_INCLUDE_PATH`: Custom path to glfw3.h
- `PHYSAC_INCLUDE_PATH`: Custom path to physac.h

## Package Variants

The project can be built as different packages:
- `raylib`: Standard desktop version
- `raylib_sdl`: SDL backend version  
- `raylib_drm`: DRM framebuffer version
- `raylib_dynamic`: Dynamic linking version (separate dynamic/ directory)

These are mutually exclusive - only one can be installed at a time.