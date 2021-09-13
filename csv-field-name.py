#!/usr/bin/env python3

import sys

args = sys.argv[1]
n = int(args[0])
comma1 = 0
comma2 = 0
trigger = 0

s = input()
i = 0
if n == 9:
   print ("State")
elif n == 0:
   print ("LatD")
else:
   while trigger != n + 1:
      if s[i] == ",":
         comma1 = comma2
         comma2 = i
         trigger = trigger + 1
      i = i + 1
   print (s[comma1 + 1:comma2])
