#!/bin/python

import math
import os
import random
import re
import sys
import functools


# Complete the superDigit function below.
def superSum(n):
    if int(n) < 10:
        return n
    n = n.replace('9', '')
    n += '9'
    if len(n) == 1:
        n = '9'
    n = functools.reduce(
        lambda a, b: a + b
        if (a + b) < 10 else (a + b) % 10 + 1, [int(tl) for tl in n])

    n = str(n)
    return n


# Complete the superDigit function below.
def superDigit(n, k):
    print(n)
    r = superSum(n)
    v = superSum(str(int(r) * k))
    #print(v)
    return v


if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    nk = raw_input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
