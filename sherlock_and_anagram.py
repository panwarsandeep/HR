#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
import operator as op
from functools import reduce
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def sherlockAndAnagrams(s):
    l = len(s)
    cnt = 0
    map = {}

    for i in range(l):
        for j in range(i,l):
            str = ""
            if i == j:
                str = s[i]
            elif i == 0:
                str = s[i:][:j+1]
            else:
                str = s[i:j+1]
            str = ''.join(sorted(str))
            if map.get(str, None):
                map[str]+= 1
            else:
                map[str] = 1
    
    for v in map.values():
        if v > 1:
            cnt += int(ncr(v, 2))
    return cnt

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
