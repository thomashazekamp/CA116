#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
number = {}

with open("translation.txt") as f:
   doc = f.read()
p = doc.split()

i = 0
while i < len(p):
   word = p[i]
   number[word] = p[i + 1]
   i = i + 2

j = 0
while j < len(words):
   first = words[j].rstrip()
   print (number[first])
   j = j + 1
