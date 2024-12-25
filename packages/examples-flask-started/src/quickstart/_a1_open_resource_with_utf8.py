"""`open_resource` with utf-8 encoding.

The content retrieved by `open_resource` must be utf-8 encoded.

Examples:
    Starting the server:
    ```shell
    flask --app src.quickstart._a1_open_resource_with_utf8.py run --debug
    ```

    Request from client:
    ```shell
    curl -v http://localhost:5000/
    curl -v http://localhost:5000/decode
    ```
"""

from typing import Any

from flask import Flask

app = Flask(__name__)


@app.route("/")
def normal_resource() -> str:
    with app.open_resource("../flaskr/schema.sql") as f:
        data = f.read()
        executescript(f.read())  # utf-8 encoded

    return f"<code>{data}</code>"


@app.route("/decode")
def decoded_resource() -> str:
    with app.open_resource("../flaskr/schema.sql") as f:
        data = f.read()
        # "str" has no attribute "decode"; maybe "encode"?
        # > script = data.decode("utf-8")
        # Argument 1 to "bytes" has incompatible type "str";
        # > script = bytes(data).decode("utf-8")
        data2: Any = data
        script = bytes(data2).decode("utf-8")
        executescript(script)

    return f"<code>{script}</code>"


@app.route("/")
def decode_resource() -> str:
    with app.open_resource("../flaskr/schema.sql") as f:
        executescript(f.read())  # utf-8 encoded

    with app.open_resource("../flaskr/schema.sql") as f:
        data = f.read()
        # "str" has no attribute "decode"; maybe "encode"?
        # > script = data.decode("utf-8")
        # Argument 1 to "bytes" has incompatible type "str";
        # > script = bytes(data).decode("utf-8")
        data2: Any = data
        script = bytes(data2).decode("utf-8")
        executescript(script)

    return f"<code>{data}</code>"


def executescript(sql_script: str, /) -> None:
    app.logger.info(sql_script)
    pass
