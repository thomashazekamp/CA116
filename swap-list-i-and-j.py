#!/usr/bin/env python3

if __name__ == "__main__":
   a = [8, 9, 4, 7, 2, 11]
   i = 1
   j = 2

p = 0
m = 0
while p < len(a) and m < 1:
   second = a[i]
   third = a[j]
   a[i] = third
   a[j] = second
   p = p + 1
   m = m + 1
