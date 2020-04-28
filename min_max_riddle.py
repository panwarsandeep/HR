#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# couple of brute-force approaches
'''
def riddle(arr):
    ln = len(arr)
    res = []
    #print(arr)
    for l in range(1,ln+1):
        tmp = []
        for i in range(ln):
            if i+l > ln:
                continue
            #print(i,l,arr[i:i+l],min(arr[i:i+l]))
            tmp.append(min(arr[i:i+l]))
        res.append(max(tmp))
        #print("max => ",res[-1])
    
    return res

def riddle(arr):
    ln = len(arr)
    res = []
    stk2 = []
    print(arr)
    stk1 = arr.copy()
    res.append(max(arr))
    itr = 0
    while len(stk1) > 1:
        maxv = 0
        print(len(stk1))
        while len(stk1) > 1:
            stk2.append(min(stk1[:2]))
            stk1 = stk1[1:]
            if stk2[-1] > maxv:
                maxv = stk2[-1]
            itr += 1
            if itr%1000 == 0:
                print(str(itr))
        stk1  = stk2
        stk2 = []
        #print(stk1)
        #print(stk2)
        res.append(maxv)
        print(res)
    
    return res


'''

'''
The logic:
- for each number, find the largest window in which the number is minimum
- create a map for all the numbers and their maximum window size in which they are minimum
- example: for input array { 2, 6, 1, 12 } the map would look like as follows:
  { 1: 4, 6: 1, 2: 2, 12: 1 }
  here the maximum window size where 1 is minimum is 4 i.e. 1 is minimum among window {2, 6, 1, 12}
  2 is mininum in the window {2, 6} hence window size = 2
  6, 12 are minimum in the windows {6} and {12} respectively hence window size 1

- Algorithm to craete the above mapping:
- - append 0 at the end of array to make the last index of the array as minimum (0 will not be part of original input array as per constraint)
- - create an empty stack
- - iterate the array from begining (left to right) for index, values => i, j
- - if stack is empty, push the tuple (value, index) into the stack
- - if the value is less than the value on top of the stack:
    - - pop the element from stack, the tuple (val, index)
    - - update the max window size for the current value in array as follows
        - if previous max window size of that element is less than the i - li + 1 where is current array index and li is the
          index of the item popped from stack.
          example: if array is: {2, 6, 1, 12} current stack is [2, 6] current index i is 2, arr[2] = 1
                   so map[1] = max(map[1], 2 - 1 + 1) => here i = 2 current idx, li = 1 (index of popped value)
                   finally map[val] where val = popped value which is 6 and its index is 1 in this case so
                   map[6] = max(map[6], 2 - 1) => here i = 2 and li = 1
        - finally push the value at ith index i.e. arr[i] with the index of the popped value i.e.
          in the above example when the stack is [(2, 0), (6, 1)] and next item '1' comes, as mentioned above the 6 will be popped out and
          after updating map for 6 and 1, again stack top (which is '2') shall be compared with 1 which is greater so 2 will be popped out and
          map for 2 and 1 shall be updated accordingly and now 1 shall be pushed to stack with index of last popped item which is '2' and whose index
          is 0, so the stack shall look like this: [(1,0)].
          when next item '12' comes, the stack will look like [(1,0), (12,3)]
          With this approach, the window in the left hand side of the number is also taken care 
    
- Once the map is ready, invert the map i.e. key, value to value,key
- e.g. {1: 4, 6: 1, 2: 2, 12: 1} to { 4: 1, 1: 6, 2: 2, 1: 12}, the thing to note here is if there are multiple values with same window
        size then take the one which has bigger number associated
- the reason of doing it is to have indexes based upon window sizes
- now start with max window size which is len(arr) and find the entry in above converted map e.g. for window size 4 the number is 1.
- append it to result array [1], now check for window size 3 and corresponding entry is not present in the map, in such cases keep the previously used value i.e. 1
  so the result array will be [1,1]
  Now check for window size 2 and the corresponding entry is present which is '2', append in the array: [1,1,2]
  check for window size 1 and the corresponding entry is present and value against it is 12 so append in result array: [1,1,2,12]
- Now just reverse the array which is the answer i.e. [12,2,1,1]

Note: Initially I thought of using insert(0) of list but one of the TC timed out, when investigated I found that insert is way more expensive than
      just append. I was trying to avoid reversing array but appened and reverse is very fast then insert.
'''
def getMapUpdated(arr):
    stack = []
    arr.append(0)
    map=defaultdict(int)
    print(arr)
    for i,j in enumerate(arr): 
        t=i
        while stack and stack[-1][0]>=j:
            val,li = stack.pop()
            map[j]=max(map[j],i-li+1)
            map[val]=max(map[val],i-li)
            print(stack)
            #print(val,i, j,map[val],map[j])
            t=li
        stack.append((j,t))
        print(stack)
    #print(d)
    del map[0]
    print(map)
    return map
    
def riddle(arr):
    ln = len(arr)
    stack = []
    map = {}
    res = []
   
    map = getMapUpdated(arr)
    #print(map)
   
    # reverse the map
    e = defaultdict(int)
    for k,v in map.items():
        e[v] = max(e[v],k)
    #print(e)
    

    i = len(arr)
    prev = 0
    while i > 1:
        # thought this would be faster but due to following 'insert' one of the test case got time limit
        # insert is way slow then append. append and then reversing arry was way faster !

        #res.insert(0,max(e[i-1],prev))
        #prev = res[0]

        res.append(max(e[i-1],prev))
        prev = res[-1]
        i -= 1
    res.reverse()
    
    return res

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()