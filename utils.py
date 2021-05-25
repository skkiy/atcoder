import math
import itertools
import math


## input
def input():
    from sys import stdin
    readline = stdin.readline
    return readline()[:-1]


## itertools
# product(list, repeat=number): nested for loop, duplicated
# combinations(list, number): nested for loop, do not duplicated
# permutations(range(N)): 順列全探索


## math
# sqrt(number):　平方根
# ceil(number): 切り上げ
# floor(number): 切り捨て
# round(number, number): 四捨五入, 位置


def enumerate_divisor(x):
    res = []
    r = math.ceil(math.sqrt(x))
    for y in range(1, r + 1):
        if x % y == 0:
            res.append(y)
            if not x / y in res:
                res.append(x / y)
    return res


def all_search(n, x):
    count = 0
    while 1:
        if n == x == 0:
            break
        for a, b, c in itertools.combinations(range(1, n + 1), 3):
            if a + b + c == x:
                count += 1

    return count


# 再帰によって2**n通りのbitの組み合わせ
def make_combination(n):
    S = [0] * n

    def rec(i):
        if i == n:
            print(S)
            return

        rec(i + 1)
        S[i] = 1
        rec(i + 1)
        S[i] = 0

    rec(0)


# bit全探索基本
def resolve(n, A, q, m):
    sum_list = []
    for i in range(n ** 2):
        total = 0
        for j in range(n):
            if int(bin(i >> j)[-1:]):
                total += A[j]
        sum_list.append(total)

    for k in m:
        print("yes" if k in sum_list else "no")


"""
R, C = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(R)])
result = 0
for p in range(2 ** R):
    # bit
    pattern = np.array(list(np.binary_repr(p).zfill(R))).astype(np.int8)
    # xorによって、裏返す
    A_ = pattern[:, None] ^ A
    # 列ごとの最大値の合計
    total = np.max([np.sum(A_ == 0, axis=0),
                    np.sum(A_ == 1, axis=0)], axis=0).sum()
    result = max(result, total)
print(result)
"""

"""
ans = 10 ** 15
for a in range(2 ** N):
    bit = np.array(list(np.binary_repr(a).zfill(N))).astype(np.int8)
    if np.count_nonzero(bit) < K:
        continue
    total = 0
    front = 0
    for i, b in enumerate(bit):
        if b:
            if A[i] > front:
                front = A[i]
            else:
                total += front + 1 - A[i]
                front += 1

        elif A[i] > front:
            front = A[i]
        elif A[i] == front:
            front += 1

    ans = min(ans, total)
"""

"""
import copy
#import numpy as np
#N = int(input())
#P = [list(map(int, input().split())) for _ in range(N)]
size = 10

patterns = list(itertools.permutations(range(size)))

#for p in P:
#    patterns = list(filter(lambda x: x[p[0]] == p[1], patterns))
def check_pattern(pattern):
    for y, x in enumerate(pattern):
        if y == size - 1:
            return True
        for move in range(1, size):
            if x + move < size and y + move < size:
                if pattern[y + move] == x + move:
                    return False
            if y + move < size and x - move >= 0 and x - move < size:
                if pattern[y + move] == x - move:
                    return False
    return True


ans = list(filter(check_pattern, patterns))
for a in ans:
    for x in a:
        text = ["Q" if x == i else "." for i in range(size)]
        print("".join(text))
    print("/////////////")
"""
