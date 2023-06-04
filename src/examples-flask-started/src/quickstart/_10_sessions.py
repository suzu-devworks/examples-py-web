"""
Sessions

server:
> flask --app src.quickstart._10_sessions run --debug
"""

from flask import Flask, redirect, request, session, url_for
from werkzeug.wrappers.response import Response as Redirect

app = Flask(__name__)


# Set the secret key to some random bytes. Keep this really secret!
# How to generate good secret keys:
# > python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = b"d02f627f72afc4acb9c4fc702eec524d5f04fcf7295dd14f711ffc0a836e6717"


@app.route("/")
def index() -> str:
    if "username" in session:
        return f'Logged in as {session["username"]}'
    return "You are not logged in"


@app.route("/login", methods=["GET", "POST"])
def login() -> str | Redirect:
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
def logout() -> Redirect:
    # remove the username from the session if it's there
    session.pop("username", None)
    return redirect(url_for("index"))
