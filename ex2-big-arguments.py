#!/usr/bin/env python3

import sys
i = 0
args = sys.argv[i:]

i = 1
while i < len(args):
   if int(args[i]) > 200:
      print (int(args[i]))
   i = i + 1
