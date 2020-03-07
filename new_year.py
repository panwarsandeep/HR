#!/bin/python3

import math
import os
import random
import re
import sys

# the idea is to find the distance between current position and ideal position of a given number
# iterate the array to find both the positions i.e. current and ideal
# Example:
# 1  2  3  4  5  6  7  8 [ideal position]
# 1  2  5  3  7  8  6  4 [real position]
# get the difference:
# Case1: if the difference is > 2 which means it is chatoic because this can't happen without giving
#         bribe more than twice
# Case2: A number has just taken bribe and moved backward (example 3,4 in above example)
# Case3: A number has both given and taken bribe so its position.
#        In the example above the number 6 has taken bribe and given as well because it is deviation from its ideal position is just '1'
#        which means, no more than 1 number greater than 6 can be ahead of 6 but thats not true, 7 and 8 are ahead of 6. So there are 2 
#        numbers (greater than 6) are ahead of 6 and its deviation is 1 from its ideal position so bribe taken by 6 = 2 - 1 = 1 time.
# Complete the minimumBribes function below.
def minimumBribes(q):
    import bisect
    dist = 0
    #print(q)
    tn = 0
    bribe = 0
    flist = []
    tmpi = 1
    for i in q:
        ai = tmpi
        ti = i
        td = ti - ai
        #print(q[i-1],ti,ai)
        if ti > ai:
            dist += td
            bribe += 1
            bisect.insort(flist, i)
            
        elif ti <= ai:
            #print("ti < ai",i+1, flist)
            tmp = ai - ti
            li = 0
            li = len(flist[bisect.bisect_right(flist, i):])
            if li > 0 and li > tmp:
                dist += li - tmp
                bribe += 1
                bisect.insort(flist, i)
        else:
            pass
        if td > 2:
            return "Too chaotic"
        tmpi += 1
    return dist


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
