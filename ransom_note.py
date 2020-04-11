#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dct = {}
    for w in magazine:
        if dct.get(w, None):
            dct[w] += 1
        else:
            dct[w] = 1
    found = True
    for w in note:
        if dct.get(w, None):
            dct[w] -= 1
        else:
            found = False
            break
    print("Yes") if found else print("No")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
