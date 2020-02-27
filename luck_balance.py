#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the luckBalance function below.
def luckBalance(k, contests):
    print(contests)
    luck = 0
    hs = 0
    winc = []
    for c in contests:
        if c[1] == 0:
            luck += c[0]
        else:
            if len(winc) == k and k > 0:
                if winc[0] < c[0]:
                    t = heapq.heappushpop(winc,c[0])
                    luck -= t
                    luck -= t
                    luck += c[0]
                else:
                    luck -= c[0]
            elif k == 0:
                luck -= c[0]
            else:
                luck += c[0]
                heapq.heappush(winc, c[0])
    print(winc)
    return luck


if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')
    print(result)

    fptr.close()
