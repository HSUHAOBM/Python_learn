import time
def timing(func):
    def wrapper():
        print("Start...")
        print('func_name',func.__name__)

        t1 = time.perf_counter()
        func()
        t2 = time.perf_counter()
        print("Elapsed time(secs):", t2 - t1)
    return wrapper

@timing
def works():
    total = 0
    for i in range(5000):
        total += i
works()