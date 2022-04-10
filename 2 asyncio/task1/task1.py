import asyncio


async def some_func():
    print('1')
    await asyncio.sleep(0)
    print('2')

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(some_func()) for i in range(2000_000)]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()

# thats was my experiment
