"""
問題:https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b
工夫する全列挙
"""

import math
import operator


def resolve(N, S):
    S = sorted(S)
    length = len(S)
    X = S[math.floor(length / 2)][0] if length % 2 == 1 else math.ceil((S[math.floor(length / 2) - 1][0] + S[math.floor(length / 2)][0]) / 2)
    S = sorted(S, key=operator.itemgetter(1))
    Y = S[math.floor(length / 2)][1] if length % 2 == 1 else math.ceil((S[math.floor(length / 2) - 1][1] + S[math.floor(length / 2)][1]) / 2)
    total = 0
    for s in S:
        total += min(abs(s[0] - X) + abs(s[1] - Y), abs(s[0] - Y) + abs(s[1] - X)) + abs(s[0] - s[1])
    return total

if __name__ == "__main__":
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    ans = resolve(N, S)
    print(ans)
