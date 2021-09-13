#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
   with open(files[i]) as f:
      check_lines = f.read()
      if files[i][len(files[i]) - 3:] == ".py" and check_lines != "":
         print (files[i])
      i = i + 1
