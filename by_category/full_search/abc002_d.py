"""
問題:https://atcoder.jp/contests/abc002/tasks/abc002_4
bit全探索
"""

import sys
import itertools
import operator
import math
import statistics


def resolve(N, M, XY):
    bit_list = [[int(bin(i >> n)[-1:]) for n in range(N)] for i in range(2 ** N)]
    max_count = 0
    for bit in bit_list:
        flag = True
        selected = [i + 1 for i, x in enumerate(bit) if x]
        for i, j in itertools.combinations(selected, 2):
            if not ([i, j] in XY or [j, i] in XY):
                flag = False
        if flag:
            max_count = max(max_count, len(selected))
    print(max_count)


if __name__ == "__main__":
    N, M = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(M)]
    resolve(N, M, XY)
