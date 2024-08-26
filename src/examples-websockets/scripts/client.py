#!/usr/bin/env python

from websockets.sync.client import connect


def hello() -> None:
    with connect("ws://localhost:8765") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {str(message)}")


hello()
