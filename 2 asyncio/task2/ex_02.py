import asyncio
import socket
import ssl
from urllib.parse import urlparse


# Fix me!
# Hint https://docs.python.org/3/library/asyncio-stream.html#get-http-headers


async def print_http_response(url: str, port: int):
    url = urlparse(url)
    context = ssl.create_default_context()
    with socket.create_connection((url.hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=url.hostname) as ssock:
            read_socket_file_obj = ssock.makefile('r')
            write_socket_file_obj = ssock.makefile('w')

            write_socket_file_obj.writelines([
                f"GET {url.path or '/'} HTTP/1.1\r\n"
                f"Host: {url.hostname}\r\n"
                f"\r\n"
            ])
            write_socket_file_obj.flush()
            while line := read_socket_file_obj.readline():
                print(f'{url.hostname} | {line}', end='')


async def main():
    resources_lst = [
        ('https://www.python.org/', 443),
        ('https://www.facebook.com/', 443)
    ]
    for url, port in resources_lst:
        await print_http_response(url, port)


if __name__ == '__main__':
    asyncio.run(main())
