#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def merge(arr, tarr, left, mid, right):
    res = 0
    i = left
    k = left
    j = mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tarr[k] = arr[i]
            i += 1
        else:
            res += mid - i + 1
            tarr[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        tarr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        tarr[k] = arr[j]
        j += 1
        k += 1
    for v in range(left, right+1):
        arr[v] = tarr[v]
    return res

def mergeSort(arr, tarr, left, right):
    res = 0
    if left < right:
        mid = (left+right)//2
        res += mergeSort(arr, tarr, left, mid)
        res += mergeSort(arr, tarr, mid+1, right)

        res += merge(arr, tarr, left, mid, right)
    return res

def countInversions(arr):
    print(arr)
    l = len(arr)
    tarr = [0]*l
    val =  mergeSort(arr, tarr, 0, l-1)
    print(arr)
    return val

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
