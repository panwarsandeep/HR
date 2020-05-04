#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxRegion function below.

def getNeighbours(i,j,m, n, visited, grid):
    # (0,0) (0,1) (0,2)
    # (1,0) (1,1) (1,2)
    # (2,0) (2,1) (2,2)
    nb = [[i-1, j-1], [i-1, j], [i-1, j+1],\
        [i, j-1], [i, j+1], \
        [i+1, j-1], [i+1, j], [i+1,j+1]]
    res = []
    for x in range(8):
        if nb[x][0] < 0 or nb[x][0] >= m or \
            nb[x][1] < 0 or nb[x][1] >= n or \
            visited[nb[x][0]][nb[x][1]] == True or \
                grid[nb[x][0]][nb[x][1]] == 0:
            pass
        else:
            res.append(nb[x])
            visited[nb[x][0]][nb[x][1]] = True
    #print("nbrs: ",res, i,j)
    return res
    
def maxRegion(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [ [False]*n for _ in range(m)]


    max_area = 0
    for i in range(m):
        for j in range(n):
            stack = []
            cnt = 0
            if visited[i][j] == False and grid[i][j] == 1:
                stack.append([i,j])
                while stack:
                    cnt += 1
                    t = stack.pop()
                    visited[t[0]][t[1]] = True
                    stack.extend(getNeighbours(t[0],t[1], m, n, visited, grid))
                #print("cnt: ",cnt)
            if max_area < cnt:
                max_area = cnt
    return max_area



if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
