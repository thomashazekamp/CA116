#!/usr/bin/env python3

import sys
sentence = sys.stdin.readlines()

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

encrypt = {}
i = 0
while i < len(src):
  src1 = src[i]
  dst1 = dst[i]
  encrypt[src1] = dst1
  i = i + 1

m = 0
while m < len(sentence):
  sent = sentence[m].rstrip()
  enc = ""
  i = 0
  while i < len(sent):
    letter = sent[i]
    if ("a" <= letter and letter <= "z") or ("A" <= letter and letter <= "Z"):
      if letter in encrypt:
        new = encrypt[letter]
    else:
      new = letter
    enc = enc + new
    i = i + 1
  m = m + 1
  print (enc)
