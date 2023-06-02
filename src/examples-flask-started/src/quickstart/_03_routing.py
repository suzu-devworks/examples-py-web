"""
Routing

server:
> flask --app src.quickstart._03_routing run --debug
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Index Page"


@app.route("/hello")
def hello() -> str:
    return "Hello, World"


"""
### Variable Rules
"""


@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return f"User {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"


"""
Unique URLs/Redirection Behavior
"""


@app.route("/projects/")
def projects():
    """
    - /projects/  -> OK.
    - /projects   -> redirect /projects/ in browser.
    """
    return "The project page"


@app.route("/about")
def about():
    """
    - /about    -> OK.
    - /about/   -> 404 “Not Found” error.
    """
    return "The about page"


"""
### URL Building
"""


"""
### HTTP Methods
"""


@app.get("/login")
def login_get():
    return show_the_login_form()


@app.post("/login")
def login_post():
    return do_the_login()


def show_the_login_form() -> str:
    return "Show the login form."


def do_the_login() -> str:
    return "Accept login."
