#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
   s = "mont"

i = 0
j = 0
while i < len(a) and j < 1:
   b = a[i]
   if b[:len(s)] == s or a[i] == s:
      print (a[i])
      j = j + 1
   i = i + 1
