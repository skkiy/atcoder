"""
問題:https://atcoder.jp/contests/abc122/tasks/abc122_b
全列挙
"""

def resolve():
    S = list(input())
    ACGT = ['A', 'C', 'G', 'T']
    ans = 0
    counts = [0] * (len(S) + 1)
    for i, s in enumerate(S):
        if s in ACGT:
            counts[i + 1] = counts[i] + 1
        else:
            counts[i + 1] = 0
    biggest = max(counts)
    if ans < biggest:
        ans = biggest

    print(ans)


if __name__ == "__main__":
    resolve()
