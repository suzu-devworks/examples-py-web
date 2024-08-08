#!/usr/bin/env python3
"""Simple https server for testing.
"""

import http.server
import socketserver
import ssl

ADDRESS = "0.0.0.0"
PORT = 8443
CERTFILE = "/etc/ssl/local/localhost.crt"
KEYFILE = "/etc/ssl/local/localhost.key"


Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer((ADDRESS, PORT), Handler) as https:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_3
    context.load_cert_chain(CERTFILE, KEYFILE)
    https.socket = context.wrap_socket(https.socket)
    ciphers = context.get_ciphers()

    print("Listening to port:", PORT)
    for cipher in ciphers:
        print("  enabled:", cipher["description"])

    try:
        https.serve_forever()
    except KeyboardInterrupt:
        pass
    https.server_close()
