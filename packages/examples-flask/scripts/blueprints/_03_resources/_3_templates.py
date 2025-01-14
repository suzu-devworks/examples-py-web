"""Templates - Blueprint Resources.

References:
    - https://flask.palletsprojects.com/en/stable/blueprints/#templates

Examples:
    Starting the server:

    ```shell
    flask --app scripts/blueprints/_03_resources/_3_templates run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/
    ```
"""

from flask import Flask


def create_app() -> Flask:
    from .admin import admin

    print("xxx", admin.static_url_path)

    app = Flask(__name__)
    app.register_blueprint(admin)

    return app
