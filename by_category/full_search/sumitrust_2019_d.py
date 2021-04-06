"""
問題:https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
工夫する全列挙
"""

def resolve(N, S):
    ans = []

    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                i = 0
                if a in S:
                    i += S.index(a)
                    if b in S[i + 1:]:
                        i += S[i + 1:].index(b)
                        if c in S[i + 2:]:
                            num = int("{}{}{}".format(a, b , c))
                            if not num in ans:
                                ans.append(num)

    return len(ans)

if __name__ == "__main__":
    N = int(input())
    S = list(map(int, list(input())))

    ans = resolve(N, S)
    print(ans)
