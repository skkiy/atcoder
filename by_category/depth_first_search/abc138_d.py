"""
https://atcoder.jp/contests/abc138/tasks/abc138_d
dfs
"""

import sys

sys.setrecursionlimit(10 ** 9)


def resolve():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for i in range(1, N):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a) # 忘れんな

    P = [0] * (N + 1)
    for i in range(1, Q + 1):
        p, x = map(int, input().split())
        P[p] += x

    counter = [0] * (N + 1)

    def _dfs(x, add, prev = 0):
        counter[x] += add

        for next_x in G[x]:
            # 逆流防止
            if next_x == prev:
                continue
            _dfs(next_x, P[next_x] + add, x)

    _dfs(1, P[1])

    print(" ".join(list(map(str, counter[1:]))))

if __name__ == "__main__":
    resolve()


"""
4 3
1 2
2 3
2 4
2 10
1 100
3 1
"""