import asyncio
import time
def a():
    for i in range(50):

        print(i)
        time.sleep(1)

async def main():
    await asyncio.sleep(2)
    print('hello')

a()
asyncio.run(main())

