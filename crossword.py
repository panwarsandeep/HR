#!/bin/python

import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
plusChar = '+'


def fixcw(cw, reverse):
    global plusChar
    for i in range(10):
        if reverse == True:
            cw[i] = [w.replace('+', plusChar) for w in cw[i]]
        else:
            for j in range(10):
                chr = cw[i][j]
                if chr != '-':
                    if chr != '+':
                        plusChar = chr
                        cw[i][j] = '+'


def crosswordPuzzle(crossword, words):
    cwentry = []

    crossword = [list(crow) for crow in crossword]
    fixcw(crossword, False)
    # row wise
    for row in range(10):
        i = 0
        crow = crossword[row]
        while i < 10:
            if crow[i] == '-' and (i == 0 or crow[i - 1] == '+'):
                sr = row
                sc = i
                len = 0
                while i < 10 and crow[i] == '-':
                    len += 1
                    i += 1
                if len > 1:
                    cwentry.append([sr, sc, len, 'H'])
            else:
                i += 1

    for col in range(10):
        i = 0
        ccol = [sub[col] for sub in crossword]
        while i < 10:
            if ccol[i] == '-' and (i == 0 or ccol[i - 1] == '+'):
                sr = i
                sc = col
                len = 0
                while i < 10 and ccol[i] == '-':
                    len += 1
                    i += 1
                if len > 1:
                    cwentry.append([sr, sc, len, 'V'])
            else:
                i += 1

    words = words.split(';')

    solveCW(crossword, cwentry, words)

    fixcw(crossword, True)
    crossword = [''.join(slist) for slist in crossword]
    return crossword


def isValid(cw, pos, word):
    sr = pos[0]
    sc = pos[1]
    l = pos[2]
    if pos[3] == 'H':
        l += sc
        i = 0
        while sc < l:
            if cw[sr][sc] == '-' or cw[sr][sc] == word[i]:
                sc += 1
                i += 1
            else:
                return False
    else:
        l += sr
        i = 0
        while sr < l:
            if cw[sr][sc] == '-' or cw[sr][sc] == word[i]:
                sr += 1
                i += 1
            else:
                return False
    return True


def deleteCrossword(cw, pos):
    sr = pos[0]
    sc = pos[1]
    len = pos[2]

    if pos[3] == 'H':
        pr = sr - 1 if sr > 0 else sr + 1
        nr = sr + 1 if sr < 9 else sr - 1
        len += sc
        while sc < len:
            if cw[pr][sc].isalpha() or cw[nr][sc].isalpha():
                pass
            else:
                cw[sr][sc] = '-'
            sc += 1
    else:
        pc = sc - 1 if sc > 0 else sc + 1
        nc = sc + 1 if sc < 9 else sc - 1
        len += sr
        while sr < len:
            if cw[sr][pc].isalpha() or cw[sr][nc].isalpha():
                pass
            else:
                cw[sr][sc] = '-'
            sr += 1


def fillCrossword(cw, pos, word):
    sr = pos[0]
    sc = pos[1]
    if pos[3] == 'H':
        i = 0
        len = sc + pos[2]
        while sc < len:
            cw[sr][sc] = word[i]
            sc += 1
            i += 1
    else:
        i = 0
        len = sr + pos[2]
        while sr < len:
            cw[sr][sc] = word[i]
            sr += 1
            i += 1


def printCrossword(cw):
    for i in range(10):
        print("")
        for j in range(10):
            print cw[i][j],


def getMatchingCwentry(cw, cwentry, word):
    l = len(word)
    match = []
    for i in range(len(cwentry)):
        if l == cwentry[i][2] and isValid(cw, cwentry[i], word):
            match.append(cwentry[i])
    return match


def solveCW(cw, cwentry, words):
    global solved
    if len(words) == 0:
        solved = True
        return True
    word = words.pop()

    cwe = None
    matches = getMatchingCwentry(cw, cwentry, word)
    for match in matches:
        fillCrossword(cw, match, word)
        cwentry.remove(match)
        solveCW(cw, cwentry, words)
        if solved:
            return True
        deleteCrossword(cw, match)
        cwentry.append(match)
    words.append(word)


if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    crossword = []

    for _ in xrange(10):
        crossword_item = raw_input()
        crossword.append(crossword_item)

    words = raw_input()
    solved = False
    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
