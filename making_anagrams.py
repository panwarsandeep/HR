#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    ad = {}
    ans = 0
    for c in a:
        if ad.get(c, None):
            ad[c] += 1
        else:
            ad[c] = 1
    for c in b:
        if ad.get(c, None):
            ad[c] -= 1
            if ad[c] == 0:
                ad.pop(c)
        else:
            ans += 1
    for v in ad.values():
        ans += v
    return ans


if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
