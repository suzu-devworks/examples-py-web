"""
Redirects and Errors

server:
> flask --app src.quickstart._08_redirects_and_errors run --debug
"""
from flask import Flask, abort, make_response, redirect, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login")
def login():
    abort(401)


@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template("error.html"), 404)
    resp.headers["X-Something"] = "A value"
    return resp
