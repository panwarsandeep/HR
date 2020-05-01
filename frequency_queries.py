#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the freqQuery function below.
def freqQuery(queries):
    from collections import defaultdict
    nums = defaultdict(int)
    freqs = defaultdict(int)
    res = []
    for q in queries:
        if q[0] == 1:
            fr = nums[q[1]]
            if fr > 0:
                freqs[fr] -= 1
            freqs[fr+1] += 1
            nums[q[1]] += 1
        elif q[0] == 2:
            if nums[q[1]] > 0:
                freqs[nums[q[1]]] -= 1
                nums[q[1]] -= 1
                freqs[nums[q[1]]] += 1
        elif q[0] == 3:
            if freqs[q[1]] > 0:
                res.append(1)
            else:
                res.append(0)
        else:
            pass

    return res

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
