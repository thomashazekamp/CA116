#!/usr/bin/env python3

s = input()
num_cities = 0
while s != "end":
   i = 0
   num_commas = 0
   while num_commas < 2 or i >= len(s):
      if s[i] == ",":
         num_commas = num_commas + 1
      if s[i] == "W" and s[i + 1] == "I":
         num_cities = num_cities + 1
      i = i + 1
   s = input()
print (num_cities)
