import time
from time import sleep
from typing import Awaitable


class MyTask:
    def __init__(self, coro):
        self.coro = coro
        self._done = False
        self._result = None
        
    def run(self):
        if not self._done:
            try:
                x = self.coro.send(None)
            except StopIteration as e:
                self._result = e.value
                self._done = True
            else:
                assert isinstance(x, Awaitable)
                func, t = x.func
                func(t)
        else:
            print('task is done')
        print('----------')


class MyAwaitable:
    def __init__(self, func):
        self.func = func

    def __await__(self):
        yield self
    

async def one_task():
    print(f'begin task')
    print('    begin big_step')
    big_result = await big_step()
    print(f'    end big_step with : {big_result}')
    print('end task')


async def big_step():
    print('        begin small_step')
    small_result = await small_step()
    print(f'        end small_step with : {small_result}')
    return small_result * 1000


async def small_step():
    print('           waiting...')
    await MyAwaitable((sleep, 2))
    print('           working...')

    return 123


t = MyTask(one_task())
t.run()
for _ in range(10):
    print('something else...')
    sleep(0.2)
t.run()