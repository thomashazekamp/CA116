#!/usr/bin/env python3

import sys

seen = {}
with open("a.txt") as f1:
   words1 = f1.read().rstrip().split()
with open("b.txt") as f2:
   words2 = f2.read().rstrip().split()

i = 0
while i < len(words1):
   word1 = words1[i]
   j = 0
   while j < len(words2):
      if word1 == words2[j]:
         if word1 not in seen:
            seen[word1] = True
      j = j + 1
   i = i + 1

for word1 in seen:
   print (word1)
