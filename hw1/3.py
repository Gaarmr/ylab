def zeros(fact):
    res = 0
    while fact > 0:
        fact //= 5
        res += fact
    return res


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
