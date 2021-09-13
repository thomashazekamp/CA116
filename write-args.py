#!/usr/bin/env python3

import sys

out_file = sys.argv[1]
in_files = sys.argv[2:]

i = 0
whole = ""
while i < len(in_files):
      indiv = in_files[i] + "\n"
      whole = whole + indiv
      i = i + 1
with open(out_file, "w") as f_out:
   f_out.write(whole)
