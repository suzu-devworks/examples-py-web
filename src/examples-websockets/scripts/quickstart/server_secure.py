#!/usr/bin/env python

import asyncio
import pathlib
import ssl

from websockets.asyncio.server import ServerConnection, serve


async def hello(websocket: ServerConnection) -> None:
    name = await websocket.recv()
    print(f"<<< {str(name)}")

    greeting = f"Hello {str(name)}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# ssl_context.load_cert_chain(localhost_pem)
localhost_crt = pathlib.Path("/etc/ssl/local/localhost.crt")
localhost_key = pathlib.Path("/etc/ssl/local/localhost.key")
ssl_context.load_cert_chain(localhost_crt, localhost_key)


async def main() -> None:
    async with serve(hello, "localhost", 8765, ssl=ssl_context):
        await asyncio.get_running_loop().create_future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
