def count_find_num(primes, limit):
    primes_prod = 1
    for p in primes:
        primes_prod *= p
    if primes_prod > limit:
        return []
    n = [primes_prod]
    for i in primes:
        o = n.copy()
        for k in o:
            l = i
            while k * l <= limit:
                n.append(k * l)
                l = l * i
        n.sort()
    return [len(n), n[-1]]
    

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []

# timeout
primesL = [263, 269, 337]
limit = 563711209520283
assert count_find_num(primesL, limit) == [15, 555749815528267]
