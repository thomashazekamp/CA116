#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
  isfile = os.path.isfile(files[i])
  if files[i][(len(files[i]) - 4):] != ".bak" and isfile is True:
    a = files[i]
    new = (files[i]) + ".bak"
    with open(a) as f:
      content = f.read()
    with open(new, "w") as f:
      f.write(content)
  i = i + 1
