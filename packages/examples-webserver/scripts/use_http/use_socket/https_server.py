import contextlib
import http.server
import socketserver
import ssl
from collections.abc import Callable
from socketserver import BaseRequestHandler, TCPServer
from typing import Any


def run(
    host: str, port: int, context: ssl.SSLContext, handler: Callable[[Any, Any, TCPServer], BaseRequestHandler]
) -> None:
    with socketserver.TCPServer((host, port), handler) as server:
        server.socket = context.wrap_socket(server.socket)

        print("Listening to port:", port)

        with contextlib.suppress(KeyboardInterrupt):
            server.serve_forever()

        server.server_close()
        print("Server stopped")


if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_3

    CERTFILE = "/etc/ssl/local/localhost.crt"
    KEYFILE = "/etc/ssl/local/localhost.key"
    context.load_cert_chain(CERTFILE, KEYFILE)

    # context.set_alpn_protocols(["h2", "http/1.1"]) * HTTP/2.0 505 ?

    handler = http.server.SimpleHTTPRequestHandler

    ciphers = context.get_ciphers()
    for cipher in ciphers:
        print("  enabled:", cipher["description"])

    run("0.0.0.0", 8443, context, handler)
