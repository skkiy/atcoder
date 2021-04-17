"""
問題:https://atcoder.jp/contests/abc077/tasks/arc084_a
二分探索
A, B, Cの三つのリストがある
a < b < cを求める
bについて、ソートされたA、Cに挿入できる位置を見つけて、その前と後ろの要素数の積の合計を求める
"""

# bisect
# a: ソート済みのリスト, x: 挿入したい要素, lo: 下限, hi: 上限
def bisect_left(a, x, lo=0, hi=None):
    # 例外処理
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2

        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


# a: ソート済みのリスト, x: 挿入したい要素, lo: 下限, hi: 上限
def bisect_right(a, x, lo=0, hi=None):
    # 例外処理
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def resolve():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))

    total_count = 0

    for b in B:
        a = bisect_left(A, b)
        c = bisect_right(C, b)
        total_count += a * (N - c)

    print(total_count)
