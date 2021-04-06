"""
問題:https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
全列挙
"""

def resolve():
    N, M = map(int, input().split())
    A = [[0] * (M + 1)] * (N + 1)

    for n in range(N):
        A[n] = list(map(int, input().split()))

    ans = 0
    for a in range(M - 1):
        for b in range(a + 1, M):
            total = sum([A[i][a] if A[i][a] > A[i][b] else A[i][b] for i in range(N)])
            if ans < total:
                ans = total

    print(ans)


if __name__ == "__main__":
    resolve()
