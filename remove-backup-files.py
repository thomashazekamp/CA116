#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
  file = files[i]
  isfile = os.path.isfile(file)
  if file[(len(file) - 4):] == ".bak" and isfile is True:
    os.unlink(file)
  i = i + 1
