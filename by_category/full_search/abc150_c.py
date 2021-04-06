"""
問題:https://atcoder.jp/contests/abc150/tasks/abc150_c
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
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

patterns = list(itertools.permutations(range(1,N + 1), N))
pi = patterns.index(P)
qi = patterns.index(Q)

print(abs(pi - qi))

