"""
問題:https://atcoder.jp/contests/abc106/tasks/abc106_b
全列挙
"""

import math


def resolve():
    N = int(input())
    ans = 0
    if N >= 105:
        for i in range(105, N + 1):
            if i % 2 == 1:
                res = []
                R = math.ceil(math.sqrt(i))
                for r in range(1, R + 1):
                    if i % r == 0:
                        res.append(r)
                        if not i / r in res:
                            res.append(i / r)
                if len(res) == 8:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    resolve()
