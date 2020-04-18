#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    i = 0
    l = len(arr)
    swaps = 0
    while i < l-1:
        while arr[i]-1 != i:
            t = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = t
            #print(arr[i], arr[arr[i]-1])
            #arr[i], arr[arr[i]-1] = arr[arr[i]-1],arr[i]
            swaps += 1
        i += 1
    return swaps
    


if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
