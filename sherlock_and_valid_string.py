#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    map = {}
    for ts in s:
        if map.get(ts,None):
            map[ts] += 1
        else:
            map[ts] = 1
    ls = list(map.values())
    ls_set = sorted(list(set(ls)))

    if len(ls_set) > 2:
        return "NO"
    elif len(ls_set) == 1:
        return "YES"
    elif len(ls_set) == 2:
        if ls.count(ls_set[0]) > 1 and ls.count(ls_set[1]) > 1:
            return "NO"
        elif (ls.count(ls_set[0]) == 1 or ls.count(ls_set[1]) == 1) \
             and ls_set[1] - ls_set[0] == 1 or \
             (ls.count(ls_set[0]) == 1 and ls_set[0] == 1):
            return "YES"
        else:
            return "NO"
    else:
        pass

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
