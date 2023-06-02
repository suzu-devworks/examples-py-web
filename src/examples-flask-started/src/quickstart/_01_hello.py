"""
A Minimal Application

server:
> flask --app src.quickstart._01_hello run --debug
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
