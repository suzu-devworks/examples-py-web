#!/usr/bin/env python

import asyncio
import pathlib
import ssl

from websockets.asyncio.client import connect

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# ssl_context.load_verify_locations(localhost_pem)
localhost_crt = pathlib.Path("/etc/ssl/local/localhost.crt")
ssl_context.load_verify_locations(localhost_crt)


async def hello() -> None:
    uri = "wss://localhost:8765"
    async with connect(uri, ssl=ssl_context) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {str(greeting)}")


if __name__ == "__main__":
    asyncio.run(hello())
