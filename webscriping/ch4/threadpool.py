import time
from concurrent.futures import ThreadPoolExecutor


def fun(name):
    for i in range(2):
        print(f'{name}:before：No, {i}//{time.perf_counter()}\n')
        time.sleep(1)
        print(f'{name}:after：No, {i}//{time.perf_counter()}\n')


if __name__ == "__main__":
    with ThreadPoolExecutor(20) as T:
        for i in range(60):
            T.submit(fun, name=f'thread{i}')
    print(time.perf_counter())