#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
'''
any given number can be appeared at following position in the triplet:
- first
- middle
- last
given any value 'v' assuming it is the last value in triplet the middle(previous) value shall be
v/r, and first value shall be v/(r*r).
take the following example:
5 5
1 5 5 25 125

initialize two dict: 'count' and 'middle' (initially both are emptty)
iterate the array:

iteration:1
value = 1
-----------------------
value | count | middle|
-----------------------
1     |  1    |  X           ==> 1 can't be in middle (1/3 == 0 and 1%3 != 0)
count = 0

iteration:2
value = 5
-----------------------
value | count | middle|
-----------------------
1     |  1    |  X      
5     |  1    |  1           ==> 5 can be in middle for 'N' triplets where 'N' is the occurances of '1's prior to this 5 which is the count of 1s
count = 0

iteration:3
value = 5 (second one)
-----------------------
value | count | middle|
-----------------------
1     |  1    |  X      
5     |  2    |  2        ==> here count of 5s becoms 2 hence the triplet in which 5 can be in middle also becomes 2
count = 0

iteration:4
value = 25
-----------------------
value | count | middle|
-----------------------
1     |  1    |  X      
5     |  2    |  2   
25    |  1    |  2     ==> 25/5 = 5 which is already present and has count 2 as middle element, hence 25 makes the triplet complete.
count = 2                  25 is 1st occurance combined witth 2 5s and 1 1s total triplet count becomes 2(middle[v] = middle.get(v,0) + count.get(k) -> here v = 25, k = 5)

iteration:5
value = 25
-----------------------
value | count | middle|
-----------------------
1     |  1    |  X      
5     |  2    |  2   
25    |  1    |  2 
125   |  1    |  1
count = 4               ==> count always depends upon the occurances calculated till middle element (in this case 25), since the last element
                            is just one occurance here. the last element's subsequent occurance will just add 1 count
                            e.g. if it would be 1 5 5 25 125 125 then total triplets would be 5 (4+1)

'''
def countTriplets(arr, r):
    triplets = 0

    count = {}
    middle = {}
    for v in arr:
        k = v//r
        #print(k,v,r)
        if middle.get(k, None) and v%r == 0:
            triplets += middle.get(k)
            #print("->",triplets)
        if count.get(k, None) and v%r == 0:
            middle[v] = middle.get(v,0) + count.get(k)
            #print("cg:",v,middle[v], count.get(k))
        
        count[v] = count.get(v,0) + 1
        #print("cnt:",v,count[v])
    
    return triplets



if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
