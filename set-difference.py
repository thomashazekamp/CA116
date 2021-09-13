#!/usr/bin/env python3

import sys

seena = {}
seenb = {}
with open("a.txt") as a_f:
   a_words = a_f.read().rstrip().split()
with open("b.txt") as b_f:
   b_words = b_f.read().rstrip().split()

i = 0
while i < len(b_words):
   b_word = b_words[i]
   if b_word not in seenb:
      seenb[b_word] = True
   i = i + 1

j = 0
while j < len(a_words):
   a_word = a_words[j]
   if a_word not in seenb:
      seena[a_word] = True
   j = j + 1

for word in seena:
   print (word)
