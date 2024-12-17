import asyncio
from time import sleep


async def start_strongman(name, power):
    print(f'силач {name} начал соревнования!')
    for i in range(1, 6):
        await asyncio.sleep(5/power)
        print(f'силач {name} поднял {i} шар...')
    print(f'силач {name} закончил соревнования!')

async def start_tournament():
    print("СОРЕВНОВАНИЯ НАЧАЛИСЬ")
    task1 = asyncio.create_task(start_strongman("Pasha", 3))
    task2 = asyncio.create_task(start_strongman("Denis", 4))
    task3 = asyncio.create_task(start_strongman("Apollon", 5))
    await task1
    await task2
    await task3
    print("КОНЕЦ СОРЕВНОВАНИЙ")

asyncio.run(start_tournament())
