"""
問題:https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e
bit全探索
"""

import numpy as np

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
