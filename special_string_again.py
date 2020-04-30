#!/bin/python3

import math
import os
import random
import re
import sys

def printMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(str(mat[i][j]) + " ", end="")
        print("")

# Complete the substrCount function below.
'''
########################################################################
Following solution works very efficiently but needs larger space N*N
therefore in this case N is 10^6 so this solution won't work.
the idea is to crate a matrix of NxN with the string represented as both row and column.
for example "abacd" shall be represended as:
     0 1 2 3 4
     a b a c d
 0  a 0 0 0 0 0
 1  b 0 0 0 0 0
 2  a 0 0 0 0 0
 3  c 0 0 0 0 0
 4  d 0 0 0 0 0

each entry in the matrix represents a substring:
example: first entry in the matrix represents the substring starting at 0 and ending at 0 i.e. 'a'
         entry at row 1, col 4 represents the substring starting at 1 and ending at 4 i.e. 'bacd'
here we keep the value 1 if the particular substring is palindrom (special string) and 0 if not.
therefore first mark the diagonal values of matrix as 1 because all single characters are palindrom (special string)
     0 1 2 3 4
     a b a c d
 0  a 1 0 0 0 0
 1  b 0 1 0 0 0
 2  a 0 0 1 0 0
 3  c 0 0 0 1 0
 4  d 0 0 0 0 1

 here substring starting at 0 and ending at 1 is same as substring starting at 1 and ending at 0 (reverse).
 therefore the matrix below and after diagonal is identical so we can simply ignore bottom part (below diagnoal)

      0 1 2 3 4
     a b a c d
 0  a 1 0 0 0 0
 1  b - 1 0 0 0
 2  a - - 1 0 0
 3  c - - - 1 0
 4  d - - - - 1

for every 2 characters long substring check if they both match, if yes then they are palendrom else not
the loop will run column wise and for each column, start row from 0 till the diagnoal value (represents the single character)

for each index in matrix i,j the bottom left entry represents the inner substring. so check if bottom left entry (i+1, j-1) is the palindrom
i.e. the matrix contains value 1 then just check first and last characters of the substring i.e. s[i] and s[j], if they both are same
this means the string is palindrom as well.

in this special case where the ask is not just to find out palindrom but some additional conditions hence some additional checks.
########################################################################

def substrCount(n, s):
    print("before init")
    mat = [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    #print(s)
    print("init done")
    for i in range(n):
        mat[i][i] = 1
        count += 1
    print("diag done")
    for j in range(n):
        for i in range(j):
            if i == j - 1 and s[i] == s[j]:
                mat[i][j] = 1
                count += 1
            elif mat[i+1][j-1] == 1 and s[i] == s[j] and i == j - 2:
                mat[i][j] = 1
                count += 1
            elif mat[i+1][j-1] == 1 and s[i] == s[j] and s[i+1] == s[i]:
                mat[i][j] = 1
                count += 1
           
            #print(i,j,mat[i][j])
    #printMat(mat)
    return count

'''


'''
#############################
The following approach works in this way:
for each character in the string keep moving in both the direction till:
    - either end of the string is reached i.e. < 0  or > len
    AND
    - characters at both the end matches
    till both the conditions are satisfied, the string is palindrom

there are two separate loop to incorporate the palindrom strings like 'baab' where the string is of even length.

some additional conditions are put which are specific for the problem i.e. special string (not simply palindrom)
#############################
'''
def substrCount(n, s):
    ans = 0
    
    #print(s,n)
    for i in range(n):
        j = 0
        while i - j >= 0 and i + j < n:
            if s[i+j] == s[i-j] and (j <= 1 or s[i+j] == s[i+j-1]):
                ans += 1
                #print(ans, i,j,s[i-j],s[i],s[i+j])
            else:
                break
            j += 1
    
    for i in range(n):
        j = 0
        while i - j >= 0 and i + j + 1< n:
            if s[i+j+1] == s[i-j] and (j < 1 or s[i+j+1] == s[i+j]):
                ans += 1
                #print(ans, i,j,s[i-j],s[i],s[i+j])
            else:
                break
            j += 1
    
    return ans

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
