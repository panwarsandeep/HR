#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    s1 = "-"+s1
    s2 = "-"+s2
    l = len(s1)


    print("init mat",l)
    mat = [ [0]*l for _ in range(l)]
    print("init mat done")
    for i in range(1,l):
        if i%1000 == 0:
            print("iteratioon: ",i)
        for j in range(1,l):
            found = 0
            if s1[i] == s2[j]:
                found = 1
            #mat[i][j] = max(max(mat[i][j-1], mat[i-1][j-1]+found), mat[i-1][j])
            
            a,b,c = mat[i][j-1], mat[i-1][j-1]+found, mat[i-1][j]
            mx = c
            if a > b:
                if a > c:
                    mx = a
            elif b > c:
                mx = b
            
            '''
            if mat[i][j-1] > mat[i-1][j-1]+found:
                mx = mat[i-1][j]
                if mat[i][j-1] > mat[i-1][j]:
                    mx = mat[i][j-1]
            else:
                mx = mat[i-1][j]
                if mat[i-1][j-1]+found > mat[i-1][j]:
                    mx = mat[i-1][j-1]+found
            '''
            mat[i][j] = mx
    return mat[l-1][l-1]

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()