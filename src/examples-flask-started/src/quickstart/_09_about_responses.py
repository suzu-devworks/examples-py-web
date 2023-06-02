"""
About Responses

server:
> flask --app src.quickstart._09_about_responses run --debug
"""
from flask import Flask, url_for

app = Flask(__name__)

"""
APIs with JSON
"""


class User(object):
    def __init__(self, username, theme, image):
        self.username = username
        self.theme = theme
        self.image = image

    def to_json(self):
        return {
            "username": self.username,
            "theme": self.theme,
            "image": url_for("static", filename=self.image),
        }


def get_current_user():
    return User("hoge", "foo", "bar")


def get_all_users():
    return [
        User("hoge1", "foo2", "bar3"),
        User("hoge1", "foo2", "bar3"),
    ]


@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("static", filename=user.image),
    }


@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]
