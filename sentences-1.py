#!/usr/bin/env python3

import sys

lines = sys.stdin.read()
word = lines.split()

i = 0
j = 0
while i < len(word):
  new_word = word[i][(len(word[i])) - 1]
  if new_word == "!" or new_word == "?" or new_word == ".":
    print (" ".join(word[j:i + 1]))
    j = i + 1
  i = i + 1
