#!/usr/bin/env python3

import sys

s = input()
count = 0

i = 0
while i < len(s) and s[i] != "'":
  if s[i] == "'":
    count = count + 1
  i = i + 1

j = i + 1
while j < len(s) and s[j] != "'":
  if s[j] == "'":
    count = count + 1
  j = j + 1
if count == 2:
  print (s[i + 1:j])
