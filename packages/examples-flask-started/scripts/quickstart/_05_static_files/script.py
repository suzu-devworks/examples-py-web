"""Static Files.

Just create a folder called static in your package or next to your module
and it will be available at /static on the application.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#static-files

Examples:
    Run the script:

    ```shell
    python scripts/quickstart/_05_static_files/script.py
    ```

    ```console
    /static/style.css
    ```
"""

from flask import Flask, url_for

app = Flask(__name__)

with app.test_request_context():
    print(url_for("static", filename="style.css"))
