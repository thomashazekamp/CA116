#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()

numbers = {
   "one": "eins",
   "two": "zwei",
   "three": "drei",
   "four": "vier",
   "five": "funf",
   "six": "sechs",
   "seven": "sieben",
   "eight": "acht",
   "nine": "neun",
   "ten": "zehn",
}
i = 0
while i < len(words):
   word = words[i].rstrip()
   print (numbers[word])
   i = i + 1
