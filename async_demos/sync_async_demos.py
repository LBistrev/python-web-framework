import asyncio
import time


async def worker1():
    # time.sleep(1)
    await asyncio.sleep(1)
    return 'bread'


async def worker2():
    # time.sleep(2)
    await asyncio.sleep(2)
    return 'cheese'


async def worker3():
    # time.sleep(3)
    await asyncio.sleep(3)
    return 'bacon'


def make_sandwich(ingredients):
    print(f'Making sandwich with {ingredients}')


async def main():
    start = time.time()

    sandwich_parts = await asyncio.gather(worker1(), worker2(), worker3())

    #  sync => total = 1 + 2 + 3 = 6
    # async => total = max(1 + 2 + 3) = 3

    make_sandwich(sandwich_parts)

    end = time.time()

    print(f'Executed in {end - start} s')


asyncio.run(main())
