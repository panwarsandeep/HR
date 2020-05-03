#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
'''
Initially tried with union find but the algorithm is not efficient and also
there is some bug, later tried with DFS

class UF:
    def __init__(self,N):
        self.id = [i for i in range(N+1)]
        self.sz = [0]*(N+1)
        #print(self.id)
    
    def _root(self, i):
        while i != self.id[i]:
            #self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i
    
    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

    def getRoots(self):
        ts = set(self.id)
        print("id: ",self.id)
        print("ts: ",ts)
        roots = []
        for t in ts:
            if t == 0:
                continue
            roots.append([t, self.id.count(t)])
        return roots

def roadsAndLibraries(n, c_lib, c_road, cities):
    uf = UF(n)
    for c in cities:
        print(c)
        uf.union(c[0],c[1])
        print(uf.id)
    roots = uf.getRoots()
    print(roots)
    cost = 0
    for r in roots:
        tc = r[1]
        if tc == 1:
            cost += c_lib
            continue

        if tc * c_lib <= (tc -1) * c_road + c_lib:
            cost += tc * c_lib
        else:
            cost += (tc -1) * c_road + c_lib
    return cost
'''

from collections import defaultdict
class Graph:
    
    def __init__(self, v):
        self.v = v
        self.adj = defaultdict(list)

    def addEdge(self, p,q):
        self.adj[p].append(q)
        self.adj[q].append(p)
    
   
    def DFS(self, visited, v):
        stack = []
        stack.append(v)
        cnt = 0
        while stack:
            it = stack.pop()
            
            if visited[it] == False:
                visited[it] = True
                cnt += 1
                for n in self.adj[it]:
                    if visited[n] == False:
                        stack.append(n)
        return cnt

    def CC(self, cl, cr):
        visited = [False for _ in range(self.v+1)]
        tmp = 0
        cost = 0
        for v in range(1, self.v+1):
            if visited[v] == False:
                tmp = self.DFS(visited, v)
                if tmp == 1:
                    cost += cl
                else:
                    if tmp * cl <= (cr * (tmp -1) + cl):
                        cost += tmp * cl
                    else:
                        cost += cr * (tmp -1) + cl
        return cost

            
def roadsAndLibraries(n, c_lib, c_road, cities):
    gr = Graph(n)
    for c in cities:
        gr.addEdge(c[0], c[1])
    return gr.CC(c_lib, c_road)



if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()