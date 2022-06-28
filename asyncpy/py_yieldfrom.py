import time
from time import sleep
class MyTask:
    def __init__(self, coro):
        self.coro = coro

    def run(self):
        while True:
            try:
                x = self.coro.send(None)
            except StopIteration as e:
                big_result = e.value
                break
            else:
                func, t = x.func
                func(t)

class MyYeildable:
    def __init__(self, func):
        self.func = func

    def __iter__(self):
        yield self

def one_task():
    print(f'begin task')
    print('    begin big_step')
    # big_result = big_step()
    big_result = yield from big_step()
    # big_coro = big_step()
    # while True:
    #     try:
    #         x = big_coro.send(None)
    #     except StopIteration as e:
    #         big_result = e.value
    #         break
    #     else:
    #         func, t = x
    #         func(t)
    print(f'    end big_step with : {big_result}')
    print('end task')

def big_step():
    print('        begin small_step')
    # small_result = small_step()
    small_result = yield from small_step()
    # small_coro = small_step()
    # while True:
    #     try:
    #         x = small_coro.send(None)
    #     except StopIteration as e:
    #         small_result = e.value
    #         break
    #     else:
    #         yield x
    print(f'        end small_step with : {small_result}')
    return small_result * 1000

def small_step():
    print('           waiting...')
    yield from MyYeildable((sleep, 2))
    print('           working...')

    return 123


t = MyTask(one_task())
t.run()
