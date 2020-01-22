import math
import os
import random
import re
import sys

# Complete the decibinaryNumbers function below.
def db_val(x):
    s = 0
    p = 1
    while x > 0:
        s += x%10 * p
        x = x/10
        p *= 2
    return s

def decibinaryNumbers(x):

    def cnt_first_one(n):
        c = 0
        while n > 0:
            if n & 0x1:
                break
            c += 1
            n /= 10
        return c

    res = {}
    res[0] = [0]
    res[1] = [1]
    res[2] = [2, 10]
    cnt = 4
    i = 3
    if x == 1:
        return 0
    elif x == 2:
        return 1
    elif x == 3:
        return 2
    elif x == 4:
        return 10
    else:
        pass

    prevcnt = 4
    while cnt < x:
        #print(i)
        prevcnt = cnt
        tset = set()
        d = 1
        na = 1
        if (i%2 == 0):
            d = 2
            na = 10
            while i-d >= i/2:
                
                print(res[i-d])
                #tts = set(map(lambda x: x + na if len(str(x)) <= cnt_first_one(d) or str(x)[cnt_first_one(d)] < 9 else -1, res[i - d]))
                #tts.remove(-1)

                #tset.update(list(map(lambda x: x + na if str(x)[cnt_first_one(d)] < 9 else -1, res[i - d])))
                for v in res[i-d]:
                    #print(str(v), cnt_first_one(d), type(v))
                    if len(str(v))-1 <= cnt_first_one(d) or int(str(v)[cnt_first_one(d)]) < 9:
                        tset.add((v+na))
                #tset.update(list(tts))
                na *= 10
                d *= 2
        for v in res[i-1]:
            if v%10 != 9:
                tset.update([v + 1])
        tset.add(int(bin(i).replace("0b", "")))
        cnt += len(tset)
        res[i] = list(sorted(tset))
        i += 1
    if cnt >= x:
        #print(res)
        #print(cnt, x, i, prevcnt)

        if prevcnt == x:
            tl = prevcnt - len(res[i-1])
            #print(tl)
            return res[i-1][x - tl-1]
        elif prevcnt < x:
            tl = x - prevcnt
            return res[i - 1][tl - 1]

        return list(sorted(res[i-1]))[x-cnt]



if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        x = int(raw_input())

        result = decibinaryNumbers(x)
        print("result",result)

        fptr.write(str(result) + '\n')

    fptr.close()


#    for i in range(101):
#            t = i * 10
#            tl = [db_val(x) for x in range(t, t+10)]
#            print(tl, t, t+10-1)