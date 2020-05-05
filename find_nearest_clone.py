#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
from collections import defaultdict

'''
For each node which is not visited already and has the desired color,
start a DFS search till:
- another same color node is found
- distance of cur node from first node is > already found dist between same color nodes

keeping weight of each edge as 1, the distance is calculated i.e.
- if dist of current node + weight is < dist from targetted node
- include that node
'''
def findShortest(n, graph_from, graph_to, ids, val):
    visited = [False]* (n+1)
    adj = defaultdict(list)
    for i in range(len(graph_from)):
        adj[graph_from[i]].append(graph_to[i]) if graph_to[i] not in adj[graph_from[i]] else None
        adj[graph_to[i]].append(graph_from[i]) if graph_from[i] not in adj[graph_to[i]] else None

    min_dist = sys.maxsize
    
    for i in range(1,n+1):
        stack = []
        if visited[i] == False and \
            ids[i-1] == val:
            dist = [sys.maxsize]*(n+1)
            dist[i] = 0
            
            stack.append(i)
            first = True
            while stack:
                t = stack.pop()
                visited[t] = True
                # if this is second node of desired color then capture the distance and exit, this would be minimum dist so far.
                # else if dist is > already available min_dist then no point in going further
                # compare the dist and update the minimum accordingly
                if (ids[t-1] == val or dist[t] >= min_dist) and first == False:
                    if min_dist > dist[t] :
                        min_dist = dist[t]
                    break
                first = False
                for nb in adj[t]:
                    # not all the neighbours need to be added.
                    # if it is not visited or if it is getting visited from far node (far neighbour from available ones) then ignore it
                    if visited[nb] == False and dist[t] + 1 < dist[nb]:
                        dist[nb] = dist[t] + 1
                        stack.append(nb)
    if min_dist == sys.maxsize:
        min_dist = -1
    return min_dist

    
if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()