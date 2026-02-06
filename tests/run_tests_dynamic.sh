#!/usr/bin/env bash

rm raylib pyray examples
ln -s ../dynamic/raylib
ln -s ../dynamic/pyray
ln -s ../examples
for FILE in test_*.py
do
  if python3 $FILE; then
      echo $FILE returned true
  else
      echo $FILE returned some error
      rm raylib pyray examples
      exit
  fi
done

# Execute pytest-style stub parity tests that do not run when files are executed directly.
python3 -m pytest test_pyray_stub_parity.py

# Ensure typing smoke checks are exercised by automation.
if command -v uv >/dev/null 2>&1; then
    uv run ty check typing/pyray_stub_smoke.py
else
    python3 -m ty check typing/pyray_stub_smoke.py
fi

rm raylib pyray examples
