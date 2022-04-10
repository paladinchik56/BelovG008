import asyncio
from commands import *

comm = {"echo\n": echo, "split\n": my_split, "$\n": saveVal, "get\n": get_saved}


async def handle(reader, writer):
    data = await reader.readline()
    rx = 0
    while data:
        message = data.decode()
        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")

        print(f"Send: {message!r}")
        # writer.write(data)
        await writer.drain()
        if message in comm:
            data = await reader.readline()
            text = data.decode()
            print(f"Received text {message!r} from {addr!r}")
            answer = comm[message](text)

            if type(answer) == str:
                writer.write(bytes(answer, "utf-8"))
            else:
                try:
                    answer = " ".join(answer)
                    writer.write(bytes(answer, "utf-8"))
                except Exception:
                    writer.write(bytes("sorry, don't can't do this command for this text", "utf-8"))

        if "$" == message[0]:
            answer = comm["$\n"](message)
            writer.write(bytes(message, "utf-8"))

        data = await reader.readline(  )

    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle, '127.0.0.1', 8889)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()


asyncio.run(main())
