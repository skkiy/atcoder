"""
問題:https://atcoder.jp/contests/abc145/tasks/abc145_c
順列全探索
"""

import itertools
import operator
import math
import statistics
import sys

sys.setrecursionlimit(10 ** 7)
import copy
import numpy as np

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

def calc_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


distances = []
for pattern in itertools.permutations(range(N)):
    total_distance = 0
    for i, _ in enumerate(range(len(pattern) - 1)):
        total_distance += calc_distance(XY[pattern[i]], XY[pattern[i + 1]])
    distances.append(total_distance)

print(np.average(distances))
