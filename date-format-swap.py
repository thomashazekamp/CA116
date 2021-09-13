#!/usr/bin/env python3

n = int(input())

firstd = n % 10
secondd = n % 100 // 10
thirdd = n % 1000 // 100
fourthd = n % 10000 // 1000
fifthd = n % 100000 // 10000
sixthd = n % 1000000 // 100000

twodig = (fourthd * 100000 + thirdd * 10000)
lastdadd = (sixthd * 1000 + fifthd * 100 + secondd * 10 + firstd * 1)
print (twodig + lastdadd)
