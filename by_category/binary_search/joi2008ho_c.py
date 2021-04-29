import itertools
from bisect import bisect


def resolve():
    D, E = map(int, input().split())
    N = [0] + [int(input()) for _ in range(D)]
    N.sort()

    scores = []
    for a, b in itertools.combinations_with_replacement(N, 2):
        c = a + b
        if c <= E:
            scores.append(c)
    scores.sort()
    ans = 0
    for s in scores:
        if s > E:
            continue
        ans = max(ans, s+scores[bisect(scores, E - s) - 1])
    print(ans)


if __name__ == "__main__":
    resolve()

"""
4 50
3
14
15
9
"""

"""
48
"""
