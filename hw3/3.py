from functools import wraps


def to_cache(func):
    cache = {}
    @wraps(func)
    def wrapper(arg):
        if arg in cache:
            return cache.get(arg)
        res = func(arg)
        cache[arg] = res
        return res
    return wrapper


@to_cache
def multiplier(number: int):
    return number * 2


print(multiplier(5))
print(multiplier(5))
print(multiplier(5))

print(multiplier(3))
print(multiplier(3))
