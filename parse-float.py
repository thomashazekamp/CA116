#!/usr/bin/env python3

f = input()
i = 0
while i < len(f) and (f[i] < "0" or "9" < f[i]):
   i = i + 1

if i < len(f):
   j = i
   while j < len(f) and ("0" <= f[j] and f[j] <= "9"):
      j = j + 1
   print (f[:j])

   while j < len(f) and (f[j] < "0" or "9" < f[j]):
      j = j + 1

   if j < len(f):
      p = j
      while p < len(f) and ("0" <= f[p] and f[p] <= "9"):
         p = p + 1
      print (f[j:p])
