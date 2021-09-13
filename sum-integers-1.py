#!/usr/bin/env python3

import sys

a = sys.stdin.readline()
b = a.rstrip()

total = 0
while b != "":
   total = total + int(a)
   a = sys.stdin.readline()
   b = a.rstrip()

print (total)
