#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
with open("banned.txt") as f:
  banned_words = f.read().strip().split()

asterix = {}
i = 0
while i < len(banned_words):
  banned_word = banned_words[i]
  if banned_word not in asterix:
    asterix[banned_word] = (len(banned_word) * "*")
  i = i + 1

i = 0
while i < len(words):
  word = words[i].rstrip().split()
  j = 0
  while j < len(word):
    if word[j] in asterix:
      word[j] = asterix[banned_word]
    j = j + 1
  z = 0
  while z < len(word):
    sentence = " ".join(word)
    z = z + 1
  print (sentence)
  i = i + 1
