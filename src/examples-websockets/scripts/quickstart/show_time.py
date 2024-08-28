#!/usr/bin/env python

import asyncio
import datetime
import random

from websockets.asyncio.server import ServerConnection, serve


async def show_time(websocket: ServerConnection) -> None:
    while True:
        message = datetime.datetime.now(datetime.UTC).isoformat() + "Z"
        await websocket.send(message)
        await asyncio.sleep(random.random() * 2 + 1)


async def main() -> None:
    async with serve(show_time, "localhost", 5678):
        await asyncio.get_running_loop().create_future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
