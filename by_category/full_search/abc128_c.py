"""
問題:https://atcoder.jp/contests/abc128/tasks/abc128_c
bit全探索
"""

def resolve(N, M, S, P):
    bit_list = [[int(bin(i >> n)[-1:]) for n in range(N)] for i in range(2 ** N)]
    res = 0
    for bit in bit_list:
        flag = True
        for m in range(M):
            count = 0
            for s in S[m]:
                if bit[s - 1]:
                    count += 1
            if not count % 2 == P[m]:
                flag = False

        if flag:
            res += 1

    print(res)


if __name__ == "__main__":
    N, M = map(int, input().split())
    S = [list(map(int, input().split()))[1:] for _ in range(M)]
    P = list(map(int, input().split()))
    resolve(N, M, S, P)
