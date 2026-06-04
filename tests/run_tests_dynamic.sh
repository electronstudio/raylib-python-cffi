#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"

cd "${SCRIPT_DIR}"

cleanup() {
    rm -f raylib pyray examples
}

cleanup
trap cleanup EXIT

ln -s ../dynamic/raylib
ln -s ../dynamic/pyray
ln -s ../examples
for FILE in test_*.py
do
  if python3 "$FILE"; then
      echo "$FILE returned true"
  else
      echo "$FILE returned some error"
      exit 1
  fi
done

# Execute pytest-style stub parity tests that do not run when files are executed directly.
PYRAY_STUB_PATH="${REPO_ROOT}/dynamic/pyray/__init__.pyi" \
    python3 -m pytest test_pyray_stub_parity.py

# Run typing smoke checks when ty is available, but do not require it.
if command -v ty >/dev/null 2>&1; then
    ty check \
        --project "${REPO_ROOT}/dynamic" \
        --extra-search-path "${REPO_ROOT}/dynamic" \
        typing/pyray_stub_smoke.py
else
    echo "Skipping typing smoke check: ty CLI is not installed."
fi
