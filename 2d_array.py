#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

# Complete the hourglassSum function below.
'''
def hourglassSum(arr):
    hg = np.array([[1,1,1], [0,1,0], [1,1,1]])
    max_sum = -math.inf
    mat = np.array(arr).reshape(6,6)
    for i in range((6-2)):
        for j in range((6-2)):
            smat = mat[i:i+3,j:j+3]
            #print(smat)
            tsum = np.sum(smat*hg)
            if tsum > max_sum:
                max_sum = tsum
    return max_sum
'''

#without using numpy
def hourglassSum(arr):
    max_sum = -math.inf
    for i in range((6-2)):
        for j in range(6-2):
            tsum = 0
            tsum += sum(arr[j][i:i+3]) # first row
            tsum += arr[j+1][i+1:i+2][0] # middle element of second row
            tsum += sum(arr[j+2][i:i+3]) #third row
            if max_sum < tsum:
                max_sum = tsum
    return max_sum


if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
