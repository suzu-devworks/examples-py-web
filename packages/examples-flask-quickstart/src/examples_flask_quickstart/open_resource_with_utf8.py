"""open_resource with utf-8 encoding.

The content retrieved by open_resource must be utf-8 encoded.

Examples:
    Starting the server:

        $ flask --app examples_flask_quickstart.open_resource_with_utf8.py run --debug

    Request from client:

        $ curl -v http://localhost:5000/
        $ curl -v http://localhost:5000/encoding
        $ curl -v http://localhost:5000/binary

"""

from typing import Any

from flask import Flask

app = Flask(__name__)


@app.route("/")
def string_resource() -> str:
    with app.open_resource("./resources/open_resource_japanese.txt", "r") as f:
        # f.read() may return either `str` (text mode) or `bytes` depending on
        # the underlying stream type. Tell mypy the possible types and ensure
        # we always pass a `str` to `executescript`.
        data: str | bytes = f.read()
        if isinstance(data, (bytes, bytearray)):
            script = data.decode("utf-8")
        else:
            script = str(data)
        executescript(script)

    return f"<code>{script}</code>"


@app.route("/encoding")
def string_encoding_resource() -> str:
    with app.open_resource("./resources/open_resource_japanese.txt", "r", encoding="utf-8") as f:
        script: str = f.read()   # utf-8 encoded
        executescript(script)

    return f"<code>{script}</code>"


@app.route("/binary")
def bytes_resource() -> str:
    with app.open_resource("./resources/open_resource_japanese.txt", "rb") as f:
        data: Any = f.read()
        script = bytes(data).decode("utf-8")    # utf-8 encoded
        executescript(script)

    return f"<code>{script}</code>"


def executescript(sql_script: str) -> None:
    app.logger.info(sql_script)
    pass
