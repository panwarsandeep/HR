#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def getMedian(arr, d):
    med = 0
    if d%2 == 0:
        med = (arr[d//2-1]+arr[d//2])/2
    else:
        med = arr[d//2]
    return med

def activityNotifications(expenditure, d):
    import bisect
    arr = sorted(expenditure[:d])
    med = getMedian(arr,d)
    res = 0
    i = 0
    for n in expenditure[d:]:
        if n >= med*2:
            res += 1
        # here list.remove is expensive as it is O(N), we need to take advantage that array is sorted.
        # therefore bisect.bisect_left is used which takes advantage of the property that array is sortted
        #arr.remove(expenditure[i])
        del arr[bisect.bisect_left(arr, expenditure[i])]
        bisect.insort(arr, n)
        med = getMedian(arr, d)
        i += 1
    return res
    

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
