#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
   s = "mont"

i = 0
while i < len(a):
   b = a[i]
   if b[:len(s)] == s or a[i] == s:
      print (a[i])
   i = i + 1
