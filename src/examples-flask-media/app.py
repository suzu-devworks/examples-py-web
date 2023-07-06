from logging import DEBUG, basicConfig
from typing import Any, Mapping

from flask import Flask, render_template


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    from examples.livecv import blueprint as livecv
    from examples.videochunks import blueprint as videochunks

    basicConfig(level=DEBUG)

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # add blueprints
    app.register_blueprint(livecv)
    app.register_blueprint(videochunks)

    @app.route("/")
    def hello() -> str:
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", threaded=True)
