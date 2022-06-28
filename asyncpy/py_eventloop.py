import collections
import heapq
import itertools
import random
import time
from time import sleep
from typing import Awaitable

task_id_counter = itertools.count(1)


class MyTask:
    def __init__(self, coro):
        self.coro = coro
        self._done = False
        self._result = None
        self._id = f'task_{next(task_id_counter)}'

    def run(self):
        print(f'----{self._id}----')
        if not self._done:
            try:
                x = self.coro.send(None)
            except StopIteration as e:
                self._result = e.value
                self._done = True
            else:
                assert isinstance(x, Awaitable)
                el.call_later(x.func, self.run)
                # func, t = x.func
                # func(t)
        else:
            print('task is done')
        print('----------')


class EventLoop:

    def __init__(self):
        self._ready = collections.deque()
        self._scheduled = []
        self._stopping = False

    def call_soon(self, callback, *args):
        self._ready.append((callback, args))

    def call_later(self, delay, callback, *args):
        t = time.time() + delay
        heapq.heappush(self._scheduled, (t, callback, args))

    def stop(self):
        self._stopping = True

    def run_once(self):
        now = time.time()
        if self._scheduled:
            if self._scheduled[0][0] < now:
                _, cb, args = heapq.heappop(self._scheduled)
                self._ready.append((cb, args))
        num = len(self._ready)
        for i in range(num):
            cb, args = self._ready.popleft()
            print(cb, args)
            cb(*args)

    def run_forever(self):
        while True:
            self.run_once()
            if self._stopping:
                break

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
    sleep_time = random.random()
    await MyAwaitable(sleep_time)
    print(f'sleep {sleep_time} seconds this time.')
    print('           working...')

    return 123

el = EventLoop()
# t = MyTask(one_task())
# el.call_soon(t.run)
# el.call_later(2, t.run)
for i in range(3):
    t = MyTask(one_task())
    el.call_soon(t.run)

el.call_later(1.1, el.stop)
el.run_forever()
