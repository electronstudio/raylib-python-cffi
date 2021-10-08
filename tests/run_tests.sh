#!/usr/bin/env bash

ln -s ../raylib
ln -s ../pyray
ln -s ../examples
for FILE in *.py
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