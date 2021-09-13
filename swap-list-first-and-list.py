#!/usr/bin/env python3

if __name__ == "__main__":
   a = [8, 9, 4, 7, 2, 11]

i = 0
j = 0
while i < len(a) and j < 1:
   first = a[0]
   last = a[len(a) - 1]
   a[len(a) - 1] = first
   a[0] = last
   i = i + 1
   j = j + 1
