import asyncio

# def hello_world(loop):
#     print('Hello World')
#     loop.stop()

# loop = asyncio.get_event_loop()

# # Schedule a call to hello_world()
# loop.call_soon(hello_world, loop)

# # Blocking call interrupted by loop.stop()
# loop.run_forever()
# loop.close()
import asyncio
import aiohttp

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    # print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))