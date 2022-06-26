def count_find_num(primes, limit):
    primes_prod = 1
    for p in primes:
        primes_prod *= p
    step = limit // primes_prod
    count = 0
    max_n = 0
    for i in range(1, step + 1):
        x = i
        for p in primes:
            while x % p == 0:
                x //= p
        if x == 1:
            count +=1
            max_n = i * primes_prod
    if count == 0:
        return []
    return [count, max_n]
    

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
