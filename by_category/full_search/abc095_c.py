"""
問題:https://atcoder.jp/contests/abc095/tasks/arc096_a
工夫する全列挙
"""

def resolve(A, B, C, X, Y):
    res = 10 ** 10
    for i in range(10 ** 5 + 1):
        res = min(res, A * max(X - i, 0) + B * max(Y - i, 0) + 2 * C * i)
    return res


if __name__ == "__main__":
    A, B, C, X, Y = map(int, input().split())

    ans = resolve(A, B, C, X, Y)
    print(ans)
