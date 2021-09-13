#!/usr/bin/env python3

timetable = []

line = input()
while line != "end":
   timetable.append(line)
   line = input()

i = 0
while i < len(timetable):
   parse = timetable[i].split()
   start = int(parse[1])
   duration = int(parse[2])
   end = start + duration - 1
   start = str(start) + ":00"
   end = str(end) + ":50"
   print (parse[0], start, end, " ".join(parse[3:]))
   i = i + 1
