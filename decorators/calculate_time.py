# funtion 使用的時間
import time
from functools import wraps
def calculate_time(place=8):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            beg = time.time()
            f = func(*args, **kwargs)
            end = time.time()
            s = '{}(){:.%sf} s' % place
            print(s.format(func.__name__, end - beg))
            return f
        return wrapper
    return decorator


@calculate_time()
def works():
    total = 0
    for i in range(500000):
        total += i
works()

def calculate_time(func):
    def wrapper():
        beg = time.time()
        func()
        end = time.time()
        print(func.__name__,end - beg)
    return wrapper

@calculate_time
def works():
    total = 0
    for i in range(500000):
        total += i
works()
