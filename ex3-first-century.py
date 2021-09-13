#!/usr/bin/env python3

import sys

input = sys.stdin.read().split()

i = 0
j = 0
num = 0
while i < len(input) and j < 1:
  if int(input[i]) >= 100:
    num = num + int(input[i])
    j = j + 1
  i = i + 1
if num == 0:
  print ("none")
else:
  print (num)
