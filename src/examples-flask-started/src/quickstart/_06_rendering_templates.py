"""
Rendering Templates

server:
> flask --app src.quickstart._06_rendering_templates run --debug
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name: str | None = None) -> str:
    return render_template("hello.html", name=name)
