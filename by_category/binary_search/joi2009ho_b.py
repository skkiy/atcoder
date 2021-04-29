"""
問題:https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b
二分探索
"""


def find(D, k):
    lo = 0
    hi = len(D)

    while lo < hi:
        mid = (lo + hi) // 2

        if k < D[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def resolve():
    d = int(input())
    n = int(input())
    m = int(input())
    D = [0]
    for _ in range(n - 1):
        D.append(int(input()))
    D.append(d)
    D.sort()

    K = []
    for _ in range(m):
        K.append(int(input()))

    K.sort()

    total = 0
    for k in K:
        i = find(D, k)
        total += min(k - D[i - 1], D[i] - k)

    print(total)

if __name__ == "__main__":
    resolve()