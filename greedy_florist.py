import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    cost = 0
    prev = -1
    for i in range(0,len(c)):
        if i%k == 0:
            prev += 1
        cost += c[i]*(prev+1)

    return cost

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
