import contextlib
import ssl
from collections.abc import Callable
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import BaseRequestHandler
from typing import Any


def run(
    host: str, port: int, context: ssl.SSLContext, handler: Callable[[Any, Any, HTTPServer], BaseRequestHandler]
) -> None:
    with HTTPServer((host, port), handler) as server:
        server.socket = context.wrap_socket(server.socket)

        print("Listening to port:", port)

        with contextlib.suppress(KeyboardInterrupt):
            server.serve_forever()

        server.server_close()
        print("Server stopped")


if __name__ == "__main__":
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    CERTFILE = "/etc/ssl/local/localhost.crt"
    KEYFILE = "/etc/ssl/local/localhost.key"

    context.load_cert_chain(CERTFILE, KEYFILE)
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1

    handler = SimpleHTTPRequestHandler

    run("0.0.0.0", 8443, context, handler)
