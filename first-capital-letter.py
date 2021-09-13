#!/usr/bin/env python3

s = input()
m = len(s)

i = 0
while i < m:
   p = s[i]
   if p == "A" or p == "B" or p == "C" or p == "D" or p == "E" or p == "F":
      print (i)
      i = m
   elif p == "G" or p == "H" or p == "I" or p == "J" or p == "K" or p == "L":
      print (i)
      i = m
   elif p == "M" or p == "N" or p == "O" or p == "P" or p == "Q" or p == "R":
      print (i)
      i = m
   elif p == "S" or p == "T" or p == "U" or p == "V" or p == "W":
      print (i)
      i = m
   elif p == "X" or p == "Y" or p == "Z":
      print (i)
      i = m
   else:
      i = i + 1
