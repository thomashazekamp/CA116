#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
similar = {}

i = 0
j = 0
while i < len(words) and j < 1:
   word = words[i].rstrip()
   if word not in similar:
      similar[word] = 0
   similar[word] = similar[word] + 1
   if similar[word] == 2:
      print ("snap:", word)
      j = j + 1
   i = i + 1
