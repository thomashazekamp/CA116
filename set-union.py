#!/usr/bin/env python3

import sys

seen = {}
with open("a.txt") as f:
   words = f.read().rstrip().split()
i = 0
while i < len(words):
   word = words[i]
   if word not in seen:
      seen[word] = True
   i = i + 1
with open("b.txt") as f:
   words = f.read().rstrip().split()
i = 0
while i < len(words):
   word = words[i]
   if word not in seen:
      seen[word] = True
   i = i + 1

for word in seen:
   print (word)
