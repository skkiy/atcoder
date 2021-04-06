"""
問題:https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_c
工夫する全列挙
結果:TLE
"""

def resolve(N, S):
    max_area = 0
    for i, o in enumerate(S[:-1]):
        for p in S[i + 1:]:
            if o >= p:
                continue
            q = [p[0] - p[1] + o[1], p[1] + p[0] - o[0]]
            r = [o[0] - p[1] + o[1], o[1] + p[0] - o[0]]
            if q in S and r in S:
                max_area = max(max_area, (o[0] - p[0]) ** 2 + (o[1] - p[1]) ** 2)

    return max_area


if __name__ == "__main__":
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    ans = resolve(N, sorted(S))
    print(ans)
