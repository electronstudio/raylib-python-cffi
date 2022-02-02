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
rm raylib pyray examples