#!/usr/bin/env python3

s = input()
n = int(input())
t = "-"

total_print = (s + t) * n
length = len(total_print)
print (total_print[0:(length - 1)])
