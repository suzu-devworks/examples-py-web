"""Be mounted at different locations - Registering Blueprints.

Blueprints however can also be mounted at different locations:

References:
    - https://flask.palletsprojects.com/en/stable/blueprints/#registering-blueprints

Examples:
    Starting the server:

    ```shell
    flask --app scripts/blueprints/_01_registering/_2_different_locations run
    ```

    Outputted to the server console:

    ```console
    Registering Blueprints:
      Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
      <Rule '/pages/' (HEAD, OPTIONS, GET) -> simple_page.show>,
      <Rule '/pages/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>]
    ```

    Request from client:

"""

from flask import Flask, redirect, url_for
from werkzeug import Response


def create_app() -> Flask:
    from my_first_blueprint.simple_page import simple_page

    app = Flask(__name__)

    app.register_blueprint(simple_page, url_prefix="/pages")
    print("Registering Blueprints:\n", app.url_map)

    # redirect to home.
    @app.route("/")
    def index() -> Response:
        return redirect(url_for("simple_page.show", page="index"))

    return app
