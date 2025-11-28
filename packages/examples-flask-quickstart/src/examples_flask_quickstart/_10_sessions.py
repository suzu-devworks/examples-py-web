"""Sessions.

References:
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions

Examples:
    Set the secret key to some random bytes. Keep this really secret!
    How to generate good secret keys::

        $ export QUICKSTART_SECRET_KEY=`python -c 'import secrets; print(secrets.token_hex())'`

    Starting the server::

        $ flask --app examples_flask_quickstart._10_sessions run --debug

    Request from client:

        $ curl -v http://localhost:5000/login

        $ curl -v http://localhost:5000/login -X POST -X POST --data-urlencode "username={your name}" -d "password={********}"
            # HTTP/1.1 302 FOUND

        $ curl -v http://localhost:5000/ -b "session={Cookie value included in login response};"
        $ curl -v http://localhost:5000/logout -b "session={Cookie value included in login response};"
            # HTTP/1.1 302 FOUND

        $ curl -v http://localhost:5000/ -b "session={Cookie value included in login response};"
            # HTTP/1.1 401 UNAUTHORIZED

"""  # noqa E501

import os

from flask import Flask, redirect, request, session, url_for
from werkzeug import Response

app = Flask(__name__)

secret_key_text = os.getenv("QUICKSTART_SECRET_KEY")
if secret_key_text:
    app.secret_key = secret_key_text.encode()
    # avoid leaving the secret text in module scope
    del secret_key_text


@app.route("/")
def index() -> str | tuple[str, int]:
    if "username" in session:
        return f'Logged in as {session["username"]}'
    return "You are not logged in", 401


@app.route("/login", methods=["GET", "POST"])
def login() -> Response | str:
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return """
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """


@app.route("/logout")
def logout() -> Response:
    # remove the username from the session if it's there
    # Not removed?
    session.pop("username", None)
    return redirect(url_for("index"))
