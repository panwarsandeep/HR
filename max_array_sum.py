import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    l = len(arr)
    dp = [0]*l
    if l == 1:
        return arr[0]
    elif l == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    else:
        prev = arr[0]
        cur = arr[1]
        dp[0] = arr[0]
        max_so_far = prev
        dp[1] = prev
        if prev < cur:
            max_so_far = cur
            dp[1] = cur

        for i in range(2,l):
            if dp[i-2]+arr[i] > max_so_far and dp[i-2]+arr[i] > arr[i]:
                dp[i] = dp[i-2]+arr[i]
                max_so_far = dp[i]
            elif max_so_far > arr[i]:
                dp[i] = max_so_far
            else:
                dp[i] = arr[i]
                max_so_far = dp[i]
        return max_so_far

if __name__ == '__main__':
    fptr = open('out.txt', 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

