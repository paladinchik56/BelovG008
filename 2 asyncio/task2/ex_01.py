import asyncio


# Fix me!


async def some_func():
    print('Before')
    await asyncio.sleep(10)
    print('After')


async def main():
    await some_func()


if __name__ == '__main__':
    asyncio.run(main())
