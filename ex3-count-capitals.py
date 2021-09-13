#!/usr/bin/env python3

import sys

word = sys.stdin.read().split()

i = 0
tot_cap = 0
while i < len(word):
  one_word = word[i]
  j = 0
  while j < len(one_word):
    if one_word[j] >= "A" and "Z" >= one_word[j]:
      tot_cap = tot_cap + 1
    j = j + 1
  i = i + 1
print (tot_cap)
