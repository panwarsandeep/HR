#!/bin/python

import math
import os
import random
import re
import sys

def solve(a,b, dp):
    import string
    la = len(a)
    lb = len(b)
    if dp[lb][la] != -1:
        return dp[lb][la]

    if a[-1] == b[-1]:
        dp[lb][la] = solve(a[:-1], b[:-1], dp)
    elif a[-1].upper() == b[-1]:
        dp[lb][la] = solve(a[:-1], b[:-1], dp) or solve(a[:-1], b, dp)
    elif a[-1].islower():
        dp[lb][la] = solve(a[:-1],b, dp)
    else:
        dp[lb][la] = 0
    return dp[lb][la]

# Complete the abbreviation function below.
def abbreviation(a, b):
    
    #dp = [[-1]*(len(a)+1)]*(len(b)+1)
    dp = [[-1 for i in range(len(a)+1)] for j in range(len(b)+1)]
    #print(dp)
    dp[0][0] = 1
    #print(dp[0][0])
    #print(dp[1][0])
    for i in range(1, len(a)+1):
        if a[i-1].islower() and dp[0][i-1] == 1:
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    for i in range(1, len(b)+1):
        dp[i][0] = 0

    #print(dp)
    if solve(a,b, dp):
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        a = raw_input()

        b = raw_input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()


""" def solve(a, b):
    import string
    la = len(a)
    lb = len(b)
    if lb == 0:
        if la == 0 or len(filter(lambda x: x in string.uppercase, a)) == 0:
            return True
        else:
            return False
    elif la == 0 and lb > 0:
        return False
    else:
        if b[-1] == a[-1]:
            return solve(a[:-1], b[:-1])
        elif b[-1] == a[-1].upper():
            return solve(a[:-1], b[:-1]) or solve(a[:-1], b)
        elif a[-1].isupper():
            return False
        else:
            return solve(a[:-1], b)
 """