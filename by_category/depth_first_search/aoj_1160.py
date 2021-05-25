"""
問題:https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp
深さ優先探索
"""

import sys
sys.setrecursionlimit(10**6)

def resolve(W, H):
    def _dfs(h, w):
        C[h][w] = 0

        for x, y in dirs:
            if w + x >= W or h + y >= H or w + x < 0 or h + y < 0:
                continue

            if not C[h + y][w + x]:
                continue

            _dfs(h + y, w + x)

    C = [list(map(int, input().split())) for _ in range(H)]
    dirs = [[1, 1], [1, 0], [1, -1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1]]
    count = 0

    for h in range(H):
        for w in range(W):
            if not C[h][w]:
                continue

            count += 1
            _dfs(h, w)

    print(count)


if __name__ == "__main__":
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break
        resolve(W, H)

"""
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
"""
