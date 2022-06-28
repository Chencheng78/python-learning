import dis
import time
"""
1. closure
"""


# example 1
def func(x):
    def inner(y):
        print(f"{x} + {y}")
        return x + y
    return inner


a = func(1)
s = a(2)
print(s)

print(func(2)(98))

def outer_func():
    loc_list = []
    def inner_func(name):
        loc_list.append(len(loc_list) + 1)
        print(f'{name} loc_list = {loc_list}')
    return inner_func

clo_func_0 = outer_func()
clo_func_0('clo_func_0')
clo_func_0('clo_func_0')
clo_func_0('clo_func_0')
clo_func_1 = outer_func()
clo_func_1('clo_func_1')
clo_func_0('clo_func_0')
clo_func_1('clo_func_1')

"""
2. decorator
"""


def timeit(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        print(time.time() - start)
        return ret
    return wrapper


def my_func(x):
    time.sleep(x)


# my_func(2)
# timeit(my_func)(2)

"""
3. decorator with args
"""


def timeit2(prefix):
    def inner(f):
        def wrapper(*args, **kwargs):
            start = time.time()
            ret = f(*args, **kwargs)
            print(f'{prefix}: ' + str(time.time() - start))
            return ret
        return wrapper
    return inner

@timeit2('time spent')
def my_func2(x):
    time.sleep(x)

# my_func2(0.2)
# timeit2('time spent')(my_func2)(0.2)

"""
4. 使用装饰器类
"""

class Timer:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        start = time.time()
        ret = self.f(*args, **kwargs)
        print(f'time: {time.time() - start}')
        return ret


# @Timer
def adding(a, b):
    time.sleep(0.1)
    return a + b

# print(adding(4,5))
# t = Timer(adding)
# t(2,4)


"""
5.装饰器类， 带参数
"""
class Timer2:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            start = time.time()
            ret = f(*args, **kwargs)
            print(f'{self.prefix}: {time.time() - start}')
            return ret
        return wrapper

# @Timer2('time spent')
def adding2(a, b):
    time.sleep(0.1)
    return a + b

# print(adding2(4,67))
# t2 = Timer2("text")(adding2)
# t2(5,7)

"""
6. 类的装饰器
"""