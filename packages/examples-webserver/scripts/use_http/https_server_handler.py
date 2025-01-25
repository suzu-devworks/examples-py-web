import contextlib
import ssl
from collections.abc import Callable
from http.server import BaseHTTPRequestHandler, HTTPServer
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


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html_context = (
            '<html lang="ja">'
            '<meta charset="UTF-8">'
            '<form method="POST" action="/"><input type="submit" value="送信"></form>'
            "</html>"
        )
        self.wfile.write(html_context.encode())

    def do_POST(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        html_context = "送信完了"
        self.wfile.write(html_context.encode())


if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_3

    CERTFILE = "/etc/ssl/local/localhost.crt"
    KEYFILE = "/etc/ssl/local/localhost.key"
    context.load_cert_chain(CERTFILE, KEYFILE)

    handler = CustomHTTPRequestHandler

    run("0.0.0.0", 8443, context, handler)
