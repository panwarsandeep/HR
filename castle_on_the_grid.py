#!/bin/python3

import math
import os
import random
import re
import sys

def getValidNeighbors(grid, visited, xx, yy, dd, dr):
    nb = []
    n = len(grid)
    #left
    
    x = xx
    y = yy
    
    #print(x,y,d)
    while y > 0 and grid[x][y-1] != 'X':
        d = dd+1 if dr != 'L' else dd
        if d < visited[x][y-1]:
            nb.append((x,y-1, d, 'L'))
            visited[x][y-1] = d
        y -= 1
    #righ
    y = yy
    while y < n-1 and grid[x][y+1] != 'X':
        d = dd+1 if dr != 'R' else dd
        if d < visited[x][y+1]:
            nb.append((x,y+1, d, 'R'))
            visited[x][y+1] = d
        y += 1
    #up
    y = yy
    while x > 0 and grid[x-1][y] != 'X':
        d = dd+1 if dr != 'U' else dd
        if d < visited[x-1][y]:
            nb.append((x-1,y, d, 'U'))
            visited[x-1][y] = d
        x -= 1
    #down
    x = xx
    while x < n-1 and grid[x+1][y] != 'X':
        d = dd+1 if dr != 'D' else dd
        if d < visited[x+1][y]:
            nb.append((x+1,y, d, 'D'))
            visited[x+1][y] = d
        x += 1
    return nb


    
# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    queue = []
    move = 0
    l = len(grid)
    visited = [[math.inf for _ in range(l)] for _ in range(l)]
    queue.append((startX, startY, 0, 'S'))
    visited[startX][startY] = 0
    while queue:
        x,y,d,dr = queue.pop(0)
        #print(x,y,d,dr)
        move += 1
        nbs = getValidNeighbors(grid, visited, x,y, d, dr)
        #print(nbs)
        if x == goalX and y == goalY:
            break
        if nbs:
            queue.extend(nbs)
    #printGrid(grid)
    #print(" ")
    #printGrid(visited)
    return visited[goalX][goalY]


def printGrid(grid):
    for i in range(len(grid)):
        for j in range (len(grid)):
            print("{} ".format(grid[i][j]), end="")
        print("")
        

if __name__ == '__main__':
    fptr = open("output.txt", 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    #print(result)
    
    fptr.write(str(result) + '\n')

    fptr.close()