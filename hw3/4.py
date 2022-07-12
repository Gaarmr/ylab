from functools import wraps
from random import randint
from time import sleep


def repeat(
    call_count,
    start_sleep_time,
    factor,
    border_sleep_time
):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = start_sleep_time
            for i in range(call_count):
                sleep(delay)
                print(f'Ожидание: {delay}')
                func(*args, **kwargs)
                if delay < border_sleep_time:
                    delay *= factor
                else:
                    delay = border_sleep_time
        return wrapper
    return decorator


@repeat(3, 1, 2, 10)
def rnd_int():
    print(randint(1, 10))


rnd_int()
