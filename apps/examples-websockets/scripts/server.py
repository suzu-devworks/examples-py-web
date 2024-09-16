#!/usr/bin/env python

import asyncio

from websockets.asyncio.server import ServerConnection, serve


async def echo(websocket: ServerConnection) -> None:
    async for message in websocket:
        print(f"<<< {str(message)}")
        await websocket.send(message)


async def main() -> None:
    async with serve(echo, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # run forever


asyncio.run(main())
