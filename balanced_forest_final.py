#!/bin/python

import math
import os
import random
import re
import sys

# Complete the balancedForest function below.
class Tree:
    def __init__(self, key, data):
        self.data = data
        self.children = {}
        self.parent = None
        self.key = key
    def addChild(self, key, node):
        self.children[key] = node
        self.data += node.data
        selfP = self.parent
        while selfP != None:
            selfP.data += node.data
            selfP = selfP.parent
        node.parent = self
    def removeChild(self, node):
        if self.children.get(node.key):
            del self.children[node.key]
            self.data -= node.data
            selfP = self.parent
            while selfP != None:
                selfP.data -= node.data
                selfP = selfP.parent
    def addParent(self, node):
        if self.parent == None:
            node.children[self.key] = self
            node.data += self.data
            self.parent = node

    def printTree(self):
        q = []
        q.append(self)
        while len(q) > 0:
            n = q.pop()
            print("(%d, %d)" % (0 if n.parent == None else n.parent.key, n.key))
            for v in n.children.values():
                q.append(v)
    def printWeights(self):
        q = []
        q.append(self)
        while len(q) > 0:
            n = q.pop()
            print("(%d, %d)" %(n.key, n.data))
            for v in n.children.values():
                q.append(v)
    def getRootNode(self):
        t = self
        while t.parent != None:
            t = t.parent
        return t


def balancedForest(c, edges):
    #print(c)
    #print(edges)
    total = sum(c)
    weights = []
    treeNodes = {}

    def getParentChield(e):
        if treeNodes[e[0]].parent == treeNodes[e[1]]:
            return treeNodes[e[1]], treeNodes[e[0]]
        else:
            return treeNodes[e[0]], treeNodes[e[1]]


    for i in range(1, len(c)+1):
        node = Tree(i, c[i-1])
        treeNodes[i] = node
    #root = treeNodes[4]
    '''
    for e in edges:
        if e[0] > e[1]:
            e[0],e[1] = e[1],e[0]
    '''
    unique = []
    flatten = [item for sublist in edges for item in sublist]
    tedges = edges[:]


    while len(tedges) > 0:
        for i in range(1, len(c)+1):
            if flatten.count(i) == 1:
                unique.append(i)
                #flatten.remove(i)
        while len(unique) > 0:
            tu = unique.pop()
            #print(tu)
            td = None
            for e in tedges:
                if tu in e:
                    #print((e[0]+e[1]-tu))
                    treeNodes[tu].addParent(treeNodes[(e[0]+e[1]-tu)])
                    td = e
                    break
            if td: tedges.remove(td)
        flatten = [item for sublist in tedges for item in sublist]
    #tedges = edges.copy()
    '''
    for i in range(1, len(c)+1):
        for e in edges:
            if i == e[0]:
                print("edges:",e, i, treeNodes[e[1]].data)
                treeNodes[i].addChild(e[1], treeNodes[e[1]])
    '''
    root = treeNodes[1].getRootNode()
    #root.printTree()
    #print("---")
    #root.printWeights()
    ans = total
    el = len(edges)
    for i in range(el):
        e = edges[i]
        #print("edges:",e)
        #tw = treeNodes[e[0]].data - treeNodes[e[1]].data
        tParent, tChild = getParentChield(e)
        tCmpNode = None
        if (tParent.data - tChild.data) >= tChild.data:
            a = tChild.data
            #itrnode = tParent
            #tw = tParent.data - tChild.data
            if a*2 == total:
                ans = a
            tParent.removeChild(tChild)
            itrnode = tParent.getRootNode()
            tw = itrnode.data
            tCmpNode = tChild
        else:
            a = tParent.data - tChild.data
            itrnode = tChild
            tw = itrnode.data
        '''
        if (treeNodes[e[0]].data - treeNodes[e[1]].data) >= treeNodes[e[1]].data:
            a = treeNodes[e[1]].data
            itrnode = treeNodes[e[0]]
            tw = treeNodes[e[0]].data - treeNodes[e[1]].data
        else:
            a = treeNodes[e[0]].data - treeNodes[e[1]].data
            itrnode = treeNodes[e[1]]
            tw = itrnode.data
        '''
        #a = treeNodes[e[0]].data - treeNodes[e[1]].data
        #itrnode = treeNodes[e[1]]

        #treeNodes[e[0]].data = treeNodes[e[0]].data - treeNodes[e[1]].data
        tq = [itrnode]
        #tw = itrnode.data
        while len(tq) > 0:
            tn = tq.pop()
            for cn in tn.children.values():
                if cn == tCmpNode:
                    continue
                tq.append(cn)
                b = tw - cn.data
                c = cn.data
                d = [a,b,c]
                tans = d.count(max(d))
                #print("d:",d)
                if tans >=2 and ans > (max(d) - min(d)):
                    if (max(d) - min(d) + total) == 3*max(d):
                        ans = max(d) - min(d)
                    #print(a,b,c,tw)
        #treeNodes[e[0]].data = treeNodes[e[0]].data + treeNodes[e[1]].data
        if tCmpNode != None:
            tParent.addChild(tCmpNode.key,tCmpNode)
    if ans == total:
        ans = -1
    #print("answer:",ans)
    return ans

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        n = int(raw_input())

        c = map(int, raw_input().rstrip().split())

        edges = []

        for _ in xrange(n - 1):
            edges.append(map(int, raw_input().rstrip().split()))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
