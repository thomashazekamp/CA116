#!/usr/bin/env python3

import sys
args = sys.argv[1]

i = 0
t = " "
while i < int(args):
   print (t * i + "#")
   i = i + 1
