import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
ts = {1: 1, 2: 2, 3: 4}


def stepPerms(n):
    s = ts.get(n)
    if s is not None:
        return ts[n]
    ts[n] = (stepPerms(n - 1) + stepPerms(n - 2) +
             stepPerms(n - 3)) % 10000000007
    return ts[n]


if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    s = int(raw_input())

    for s_itr in xrange(s):
        n = int(raw_input())

        res = stepPerms(n)
        print(res)
        fptr.write(str(res) + '\n')

    fptr.close()