"""
問題:https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja
二分探索
"""

import statistics

def find(L,X):
    median = statistics.median(L)

    if X == median:
        return True
    elif len(L) == 1:
        return False
    elif X < median:
        return find(L[:round(len(L) / 2)], X)
    else:
        return find(L[round(len(L) / 2):], X)


def resolve():
    N = int(input())
    S = list(map(int, input().split()))
    Q = int(input())
    T = list(map(int, input().split()))

    count = 0

    for t in T:
        if find(S,t):
            count += 1

    print(count)
