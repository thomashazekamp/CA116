#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

dict = {}

i = 0
while i < len(lines):
  line = lines[i].split()
  first_word = line[0]
  second_word = line[1]
  if first_word not in dict:
    dict[first_word] = second_word
  i = i + 1

i = 0
while i < len(lines):
  p = i
  j = i + 1
  while j < len(lines):
    if lines[j] < lines[p]:
      p = j
    j = j + 1

  tmp = lines[p]
  lines[p] = lines[i]
  lines[i] = tmp

  i = i + 1
print (dict)
