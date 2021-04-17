"""
問題:https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b
二分探索
"""

import statistics

def find(D, k):
    median = statistics.median(D)

    if len(D) == 3:
        return min(abs(D[0] - k), abs(D[1] - k), abs(D[2] - k))
    elif k < median:
        return find(D[:round(len(D) / 2) + 1], k)
    else:
        return find(D[round(len(D) / 2) - 1:], k)


def calc_distance(d,n,m,D,k):
    return find(D, k)


def resolve():
    d = int(input())
    n = int(input())
    m = int(input())
    D = [0]
    for _ in range(n - 1):
        D.append(int(input()))
    D.append(d)
    D = sorted(D)

    K = []
    for _ in range(m):
        K.append(int(input()))

    K = sorted(K)

    total = 0
    for k in K:
        total += find(D,k)

    print(total)
    #print(D)