#!/usr/bin/env python3

timetable = []

s = input()
while s != "end":
   timetable.append(s)
   s = input()
n = input()
i = 0
while i < len(timetable):
   tokens = timetable[i].split()
   if tokens[0] == n:
      print (" ".join(tokens))
   i = i + 1
