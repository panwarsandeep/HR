#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    ts = []
    for c in s:
        if c in ['{', '[', '(']:
            ts.append(c)
        else:
            if ts:
                pc = ts.pop()
            else:
                ts.append(c)
                break
            if (c == '}' and pc == '{' )or \
               (c == ']' and pc == '[' )or \
               (c == ')' and pc == '('):
                continue
            else:
                return "NO"
    if ts:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
