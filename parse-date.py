#!/usr/bin/env python3

s = input()
i = 0
while i < len(s) and (s[i] < "A" or s[i] > "Z"):
   i = i + 1

if i < len(s):
   j = i
   while j < len(s) and (s[j] != " "):
      j = j + 1
   day = s[i:j]

   while i < len(s) and (s[i] < "0" or "9" < s[i]):
      i = i + 1
   if i < len(s):
      j = i
      while j < len(s) and (s[j] != " "):
         j = j + 1
      day_num = s[i:j]

      while i < len(s) and (s[i] < "A" or s[i] > "Z"):
         i = i + 1
      if i < len(s):
         j = i
         while j < len(s) and (s[j] != ","):
            j = j + 1
         month = s[i:j]

         while i < len(s) and (s[i] < "0" or "9" < s[i]):
            i = i + 1
         if i < len(s):
            j = i
            while j < len(s) and (s[j] != " "):
               j = j + 1
            year = s[i:j]
   print (month, day_num + ",", year, "(" + day + ")")
