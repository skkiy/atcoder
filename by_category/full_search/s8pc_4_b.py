"""
問題:https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b
bit全探索
"""

import numpy as np

N, K = map(int, input().split())
A = list(map(int, input().split()))

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

print(ans)
