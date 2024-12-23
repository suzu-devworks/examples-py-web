#!/usr/bin/env python

import asyncio
import datetime
import random
from typing import Set

from websockets.asyncio.server import ServerConnection, broadcast, serve

CONNECTIONS: Set[ServerConnection] = set()


async def register(websocket: ServerConnection) -> None:
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)


async def show_time() -> None:
    while True:
        message = datetime.datetime.now(datetime.UTC).isoformat() + "Z"
        broadcast(CONNECTIONS, message)
        await asyncio.sleep(random.random() * 2 + 1)


async def main() -> None:
    async with serve(register, "localhost", 5678):
        await show_time()


if __name__ == "__main__":
    asyncio.run(main())
