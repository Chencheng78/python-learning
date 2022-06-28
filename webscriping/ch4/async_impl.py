import asyncio
import time


async def fun(name):
    for i in range(2):
        print(f'{name}:before：No, {i}//{time.perf_counter()}\n')
        await asyncio.sleep(1)
        print(f'{name}:after：No, {i}//{time.perf_counter()}\n')
    return name


async def main():
    print('main start')
    task_list = []
    for i in range(3):
        name = f'async{i}'
        task_list.append(asyncio.ensure_future(fun(name)))
    done, pending = await asyncio.wait(task_list, timeout=2)
    print(done)


if __name__ == "__main__":
    asyncio.run(main())
    print(time.perf_counter())