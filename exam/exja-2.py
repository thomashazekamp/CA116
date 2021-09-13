#!/usr/bin/env python3

import sys
number = sys.argv[1]

inputs = sys.stdin.readlines()

i = 0
while i < len(inputs):
  input = int(inputs[i])
  if (input % 100) != int(number) and (input % 10) != int(number):
    print (input)
  i = i + 1
