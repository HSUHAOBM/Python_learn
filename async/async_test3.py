# import asyncio
# import time

# now = lambda: time.time()

# async def dosomething(num):
#     print('第 {} 任務，第一步'.format(num))
#     await asyncio.sleep(2)
#     print('第 {} 任務，第二步'.format(num))

# if __name__ == "__main__":
#     start = now()
#     tasks = [dosomething(i) for i in range(100)]
#     asyncio.run(asyncio.wait(tasks))
#     print('TIME: ', now() - start)



# import asyncio

# async def hello_world(x):
#     print('hello_world x' + str(x))
#     await asyncio.sleep(x)

# asyncio.run(hello_world(2))


# import time

# def dosomething(i):
#     print(f"第 {i} 次開始")
#     time.sleep(2)
#     print(f"第 {i} 次結束")

# if __name__ == "__main__":
#     start = time.time()
#     for i in range(5):
#         dosomething(i+1)
#     print(f"time: {time.time() - start} (s)")



import time
import asyncio

async def dosomething(i):
    print(f"第 {i} 次開始")
    await asyncio.sleep(2)
    print(f"第 {i} 次結束")

if __name__ == "__main__":
    start = time.time()
    tasks = [dosomething(i+1) for i in range(5)]
    print(tasks)
    asyncio.run(asyncio.wait(tasks))
    print(f"time: {time.time() - start} (s)")