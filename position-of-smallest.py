#!/usr/bin/env python3

if __name__ == "__main__":
   a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]

i = 0
smallest = a[i]
pos_num = 0
while i < len(a):
   i = i + 1
   next = a[i]
   if next < smallest:
      smallest = next
      pos_num = i
   i = i + 1
print (pos_num)
