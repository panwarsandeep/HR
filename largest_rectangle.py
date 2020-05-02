#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = []
    max = 0
    for i in range(len(h)):
        if not stack or h[stack[-1]] <= h[i]:
            stack.append(i)
        else:
            while stack and h[stack[-1]] > h[i]:
                te = stack.pop()
                if not stack:
                    tm = h[te]*i
                else:
                    tm =  h[te] * (i-stack[-1]-1)
                if  tm > max:
                    max = tm
                
            stack.append(i)
        
    i += 1
    while stack:
        te = stack.pop()
        if not stack:
            tm = h[te]*i
        else:
            tm = h[te]*(i - stack[-1] -1)
        if tm > max:
            max = tm
    
    return max


if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()