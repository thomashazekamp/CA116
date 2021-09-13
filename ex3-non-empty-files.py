#!/usr/bin/env python3

import sys

files = sys.argv[1:]

i = 0
while i < len(files):
  file = files[i]
  with open(file) as f:
    check_file = f.read()
  if check_file != "":
    print (file)
  i = i + 1
