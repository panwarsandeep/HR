#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()

    tarr = arr
    a = tarr[0]
    absv = abs(a)

    for i in range(1, len(tarr)):
        b = tarr[i]
        if abs(a-b) < absv:
            absv = abs(a-b)
        a = b
    return absv

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()