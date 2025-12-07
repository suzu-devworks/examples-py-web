from logging import DEBUG, basicConfig
from typing import Any, Mapping

from flask import Flask, render_template


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:

    basicConfig(level=DEBUG)

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def index() -> str:
        return render_template("index.html")

    return app
