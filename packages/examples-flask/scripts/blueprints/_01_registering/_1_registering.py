"""Registering Blueprints.

So how do you register that blueprint? Like this:

References:
    - https://flask.palletsprojects.com/en/stable/blueprints/#registering-blueprints

Examples:
    Starting the server:

    ```shell
    flask --app scripts/blueprints/_01_registering/_1_registering run
    ```

    Outputted to the server console:

    ```console
    Registering Blueprints:
      Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
      <Rule '/' (HEAD, OPTIONS, GET) -> simple_page.show>,
      <Rule '/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>]
    ```

"""

from flask import Flask


def create_app() -> Flask:
    from my_first_blueprint.simple_page import simple_page

    app = Flask(__name__)

    app.register_blueprint(simple_page)
    print("Registering Blueprints:\n", app.url_map)

    return app
