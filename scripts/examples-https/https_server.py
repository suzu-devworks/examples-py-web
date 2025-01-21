# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import contextlib
import ssl
from collections.abc import Callable
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import BaseRequestHandler
from typing import Any

HOST = "0.0.0.0"
PORT = 58443
CERTFILE = "/etc/ssl/local/localhost.crt"
KEYFILE = "/etc/ssl/local/localhost.key"


def run(
    host: str, port: int, context: ssl.SSLContext, handler: Callable[[Any, Any, HTTPServer], BaseRequestHandler]
) -> None:
    with HTTPServer((host, port), handler) as server:
        server.socket = context.wrap_socket(server.socket)

        print("Listening to port:", PORT)

        with contextlib.suppress(KeyboardInterrupt):
            server.serve_forever()

        server.server_close()
        print("Server stopped")


if __name__ == "__main__":
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(CERTFILE, KEYFILE)
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1

    # context.set_alpn_protocols(["h2", "http/1.1"]) * HTTP/2.0 505 ?

    handler = SimpleHTTPRequestHandler

    run(HOST, PORT, context, handler)
