"""
Redirects and Errors

server:
> flask --app src.quickstart._08_redirects_and_errors run --debug
"""
from typing import Any

from flask import Flask, Response, abort, make_response, redirect, render_template, url_for
from werkzeug.wrappers.response import Response as Redirect

app = Flask(__name__)


@app.route("/")
def index() -> Redirect:
    return redirect(url_for("login"))


@app.route("/login")
def login() -> Response:
    abort(401)


@app.errorhandler(404)
def page_not_found(error: Any) -> Response:
    resp = make_response(render_template("error.html"), 404)
    resp.headers["X-Something"] = "A value"
    return resp
