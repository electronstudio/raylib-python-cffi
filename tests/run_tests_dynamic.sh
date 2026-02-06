#!/usr/bin/env bash

set -euo pipefail

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
python3 -m pytest test_pyray_stub_parity.py

# Run typing smoke checks when ty is available, but do not require it.
if python3 -c "import ty" >/dev/null 2>&1; then
    python3 -m ty check typing/pyray_stub_smoke.py
else
    echo "Skipping typing smoke check: ty is not installed."
fi
