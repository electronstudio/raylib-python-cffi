# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **raylib-python-cffi** (version 6.0.1.0), Python CFFI bindings for Raylib 6.0 game development library. It provides two main Python modules:
- `raylib`: Direct C API bindings (exact copy of C functions)
- `pyray`: More Pythonic API wrapper

Also includes bindings for raymath, raygui, rlgl, physac, and GLFW.

## Key Architecture

- `/raylib/`: Core static CFFI bindings module with build system
  - `build.py` — Main CFFI build entry point; parses C headers and generates bindings
  - `__init__.py` — Module init, loads compiled CFFI extension
  - `colors.py`, `enums.py`, `defines.py` — Generated Python constants
- `/pyray/`: Pythonic wrapper API module around `raylib`
- `/dynamic/`: Dynamic binding version (separate `raylib_dynamic` package)
  - `setup.py` — Separate setuptools config for dynamic build
  - `raylib/__init__.py` — Runtime-loaded dynamic bindings
- `/examples/`: Python example code organized by category (core, textures, shapes, models, shaders, physics, audio, raygui, extra)
- `/tests/`: Test scripts for both static and dynamic versions
- `/raylib-c/`: Embedded Raylib C library source (git submodule)
- `/raygui/`: Embedded raygui C library source (git submodule)
- `/physac/`: Embedded physac physics library source
- `/docs-src/`: Sphinx documentation source
- `/docs/`: Pre-built HTML documentation (hosted on GitHub Pages)
- `setup.py` — Main setuptools entry point for static builds
- `version.py` — Single source of truth for package version

## Build System

The project uses CFFI with setuptools. Main build entry point is `raylib/build.py` which:
- Parses C headers from embedded libraries (`raylib-c/src/raylib.h`, etc.)
- Generates CFFI bindings (`_raylib_cffi.c`)
- Compiles platform-specific extension modules
- Handles platform-specific linking (Desktop/SDL/DRM backends)
- Supports environment variable customization for build paths

### Package names by platform
- Default: `raylib`
- SDL backend: `raylib_sdl`
- DRM backend: `raylib_drm`
- Software rendering (SDL): `_software` (name suffix)

## Development Commands

### Building from source
```bash
# Build Python library manually (generates CFFI bindings + compiles)
python3 raylib/build.py

# Build wheel distribution
pip3 install wheel
python3 setup.py bdist_wheel

# Install from wheel
pip3 install dist/raylib*.whl
```

### Testing
```bash
# Run main static test suite
cd tests && ./run_tests.sh

# Run dynamic version tests
cd tests && ./run_tests_dynamic.sh

# Individual test files
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

- `RAYLIB_PLATFORM`: Desktop (default), SDL, DRM, PLATFORM_COMMA, SDL_SOFT
- `RAYLIB_LINK_ARGS`: Manual linker arguments instead of pkg-config
- `RAYLIB_INCLUDE_PATH`: Custom path to `raylib.h`
- `RAYGUI_INCLUDE_PATH`: Custom path to `raygui.h`
- `GLFW_INCLUDE_PATH`: Custom path to `glfw3.h`
- `PHYSAC_INCLUDE_PATH`: Custom path to `physac.h`
- `PKG_CONFIG_LIB_raylib`: pkg-config package name for raylib (default `raylib`)
- `PKG_CONFIG_LIB_raygui`: pkg-config package name for raygui (default `raygui`)

## Package Variants

The project publishes multiple mutually exclusive PyPI packages:
- `raylib`: Standard desktop version
- `raylib_sdl`: SDL backend version
- `raylib_drm`: DRM framebuffer version
- `raylib_dynamic`: Dynamic linking version (separate `dynamic/` directory)

Only one can be installed at a time.

## GitHub Actions Workflows

### `.github/workflows/build.yml`

The main CI/CD workflow. Triggered on push, pull request, and manual dispatch.

**Jobs:**
- `build-mac-intel` — macOS Intel runners (`macos-15-intel`), Python 3.7–3.14 + PyPy 3.11, Desktop/SDL platforms
- `build-mac-arm64` — macOS ARM64 (`macos-14`), Python 3.10–3.14, Desktop/SDL platforms
- `build-linux` — Ubuntu 16 container (`electronstudio/ubuntu16-modern`), Python 3.7–3.14 + PyPy 3.11, Desktop/SDL/DRM/SDL_SOFT platforms
- `build-linux32` — 32-bit Ubuntu 16 container, same Python versions and platforms
- `build-linux-arm64` — Ubuntu ARM64 (`ubuntu-22.04-arm`), Python 3.10–3.14, Desktop/SDL/SDL_SOFT
- `build-linux-arm64-drm` — Raspberry Pi OS containers (Bullseye/Bookworm), Python 3.10–3.14, DRM only
- `build-windows` — Windows Server 2022, Python 3.7–3.14 + PyPy 3.11, Desktop/SDL/SDL_SOFT, x64
- `build-windows32` — Windows Server 2022, same Python versions, x86
- `source-distro` — Builds and publishes sdist
- `dynamic-distro` — Builds and publishes `raylib_dynamic` sdist
- `merge` — Merges all artifact uploads

**Manual dispatch inputs:**
- `publish_to_pypi` (boolean): Publish wheels to PyPI after build. Requires `PYPI_KEY` secret.

All build jobs perform a smoke test after building: `import pyray; pyray.init_window(100,100,"test")`, checking output for `"INFO: Initializing raylib"`.

### `.github/workflows/test_pypi.yml`

On-demand workflow to verify packages work when installed directly from PyPI. Triggered manually via `workflow_dispatch`.

**Inputs:**
- `package_name` (string): Which package to test (`raylib`, `raylib_sdl`, `raylib_drm`, `raylib_dynamic`) — default `raylib`
- `version` (string): Specific version to install (e.g., `5.5.0.2`) — leave empty for latest
- `pre_release` (boolean): Whether to pass `--pre` to pip to allow pre-release versions

**Matrix:**
- OS: macOS Intel (`macos-15-intel`) and macOS ARM64 (`macos-14`)
- Python versions: 3.10, 3.11, 3.12, 3.13, 3.14
- Python source: Homebrew (`brew install python@X.Y`) and python.org (`actions/setup-python`)

The workflow installs the selected package from PyPI and runs the same smoke test (`import pyray; pyray.init_window(...)`) to verify the installed wheel works correctly.

## Testing Structure

- `test_*.py` — Standard tests (run by `run_tests.sh`)
- `xtest_*.py` — Extra/manual tests (not run by default scripts)
- `test_hello_world.py` — Minimal smoke test for basic import and window init
- `test_pyray.py` — Tests the `pyray` wrapper API
- `test_static_with_only_api_from_dynamic.py` — Ensures static API matches dynamic
- `test_color.py`, `test_float_pointers.py` — Type/struct sanity checks
- `test_gamepad.py`, `test_raygui_style.py` — Feature-specific tests

## Documentation

- Source: `/docs-src/` (Sphinx reStructuredText)
- Built output: `/docs/` (HTML, committed for GitHub Pages)
- Hosted at: https://electronstudio.github.io/raylib-python-cffi
- `make_docs.sh` regenerates `/docs/` from `/docs-src/`

## Notes for Contributors

- The `version.py` file is the single source of truth for the package version.
- CFFI bindings are generated at build time from headers in `raylib-c/src/`, `raygui/src/`, `physac/src/`.
- Submodules must be initialized (`git submodule update --init --recursive`) before building.
- The `raygui.h.diff` patch is applied in CI to fix a raygui bug before compilation.
