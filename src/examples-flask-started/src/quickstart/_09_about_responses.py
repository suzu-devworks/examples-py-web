"""
About Responses

server:
> flask --app src.quickstart._09_about_responses run --debug
"""
from typing import Any

from flask import Flask, url_for

app = Flask(__name__)

"""
APIs with JSON
"""


class User(object):
    def __init__(self, username: str, theme: str, image: str) -> None:
        self.username = username
        self.theme = theme
        self.image = image

    def to_json(self) -> dict[str, Any]:
        return {
            "username": self.username,
            "theme": self.theme,
            "image": url_for("static", filename=self.image),
        }


def get_current_user() -> User:
    return User("hoge", "foo", "bar")


def get_all_users() -> list[User]:
    return [
        User("hoge1", "foo2", "bar3"),
        User("hoge1", "foo2", "bar3"),
    ]


@app.route("/me")
def me_api() -> dict[str, Any]:
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("static", filename=user.image),
    }


@app.route("/users")
def users_api() -> list[dict[str, Any]]:
    users = get_all_users()
    return [user.to_json() for user in users]
