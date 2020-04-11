#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    c = s[0]
    deletion = 0
    ls = len(s)
    ind = 1
    while ind < ls:
        while ind < ls and s[ind] == c:
            ind += 1
            deletion += 1
        if c == 'A':
            c = 'B'
        else:
            c = 'A'
        ind += 1
    
    return deletion

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
