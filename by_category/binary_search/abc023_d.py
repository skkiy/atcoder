"""
問題:https://atcoder.jp/contests/abc023/tasks/abc023_d
二分探索
"""


def judge(HS, mid):
    data = []
    for hs in HS:
        [h, s] = hs
        lim_time = (mid - h) // s
        data.append(lim_time)

    data.sort()

    for i, t in enumerate(data):
        if i > t:
            return False

    return True

def resolve():
    N = int(input())
    HS = [list(map(int, input().split())) for _ in range(N)]

    lo = 0
    hi = max(map(lambda xy: xy[0] + xy[1] * N, HS))

    while hi - lo > 1:
        mid = (lo + hi) // 2
        if judge(HS, mid):
            hi = mid
        else:
            lo = mid

    print(hi)


if __name__ == "__main__":
    resolve()

"""
4
5 6
12 4
14 7
21 2

23
"""
