P = float(input())

def get_time(f):
    return f + P / 2 ** (f / 1.5)


def binary_search():
    lo, hi = 0, 100
    while abs(hi - lo) > 10 ** (-8):
        t1 = (lo * 2 + hi) / 3
        t2 = (lo + hi * 2) / 3
        if get_time(t1) < get_time(t2):
            hi = t2
        else:
            lo = t1
    return lo


def resolve():
    res = get_time(binary_search())
    print(res)


if __name__ == "__main__":
    resolve()
