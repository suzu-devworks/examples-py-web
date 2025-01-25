#!/usr/bin/env python

"""Client using the asyncio API."""

import asyncio

from websockets.asyncio.client import connect


async def hello() -> None:
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        message = await websocket.recv()
        print(f"Received: {str(message)}")


if __name__ == "__main__":
    asyncio.run(hello())
