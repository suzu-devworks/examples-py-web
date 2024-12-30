from collections.abc import Mapping
from typing import Any

from flask import Flask, render_template

from ._02_registering import registering
from ._03_nesting import parent
from ._04_resources import resources
from ._05_building_urls import bp as building_urls
from .simple_page import simple_page


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    # app.register_blueprint(simple_page)
    app.register_blueprint(simple_page, url_prefix="/pages")

    app.register_blueprint(registering)
    print("Registering Blueprints:\n", app.url_map)

    app.register_blueprint(parent)
    app.register_blueprint(resources)
    app.register_blueprint(building_urls)

    @app.route("/")
    def index() -> str:
        return render_template("index.html")

    return app
