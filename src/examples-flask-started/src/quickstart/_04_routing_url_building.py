"""
URL Building

server:
> flask --app src.quickstart._04_routing_url_building run --debug

test request context:
> python src.quickstart/_04_routing_url_building.py
"""

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/login")
def login():
    return "login"


@app.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"


if __name__ == "__main__":
    with app.test_request_context():
        print(url_for("index"))
        print(url_for("login"))
        print(url_for("login", next="/"))
        print(url_for("profile", username="John Doe"))
