import time
import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        print(f'Силач {name} поднял {i} шар')
        await asyncio.sleep(2 / power)
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    print("Старт")
    a1 = asyncio.create_task(start_strongman('Александр', 1))
    a2 = asyncio.create_task(start_strongman('Валентин', 2))
    a3 = asyncio.create_task(start_strongman('Сергей', 1))
    await a1
    await a2
    await a3
    print("Финиш")


start = time.time()
asyncio.run(start_tournament())
finish = time.time()

print(f'Соревнования подошли к концу!')
