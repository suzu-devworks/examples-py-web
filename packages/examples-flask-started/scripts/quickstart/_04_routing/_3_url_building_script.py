"""URL Building.

To build a URL to a specific function, use the url_for() function.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#url-building

Examples:
    Run the script:

    ```shell
    python scripts/quickstart/_04_routing/_3_url_building_script.py
    ```

    ```console
    /
    /login
    /login?next=/
    /user/John%20Doe
    ```
"""

from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "index"


@app.route("/login")
def login() -> str:
    return "login"


@app.route("/user/<username>")
def profile(username: str) -> str:
    return f"{escape(username)}'s profile"


with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username="John Doe"))
