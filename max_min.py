#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.

def maxMin(k, arr):
    tarr = sorted(arr)
    min = tarr[-1] - tarr[0]
    print(tarr)
    for i in range(len(tarr) - k+1):
        print(i,tarr[i+k-1], tarr[i],min)
        if tarr[i+k-1] - tarr[i] < min:
            min = tarr[i + k - 1] - tarr[i]

    return min
'''
def maxMin(k, arr):
    import heapq
    tarr = [i*-1 for i in arr[:k]]

    heapq.heapify(tarr)

    for v in arr[k:]:
        if v < -1*tarr[0]:
            heapq.heappushpop(tarr, (v*-1))
        print(tarr, v)
    tarr = [i * -1 for i in tarr]
    return max(tarr) - min(tarr)
'''

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
