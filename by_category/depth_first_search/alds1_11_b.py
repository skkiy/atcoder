"""
問題:https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp
深さ優先探索
"""

count = 0

def resolve():
    N = int(input())
    U = []
    K = []
    V = []
    for i in range(N):
        temp = list(map(int, input().split()))
        U.append(temp[0])
        K.append(temp[1])
        V.append(temp[2:])

    D = [0] * N
    F = [0] * N

    seen = [False] * N

    def _dfs(G, v):
        global count
        seen[v] = True

        for next_v in G[v]:
            if seen[next_v - 1]:
                continue

            count += 1
            D[next_v - 1] = count
            _dfs(G, next_v - 1)

        count += 1
        F[v] = count

    for i in range(N):
        global count
        if seen[i]:
            continue

        count += 1
        D[i] = count
        _dfs(V, i)

    for i in range(N):
        print(i + 1, D[i], F[i])

if __name__ == "__main__":
    resolve()

"""
6
1 2 2 3
2 2 3 4
3 1 5
4 1 6
5 1 6
6 0
"""
