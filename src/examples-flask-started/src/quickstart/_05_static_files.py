"""
Static Files

test request context:
> python src.quickstart/_05_static_files.py
"""

from flask import Flask, url_for

app = Flask(__name__)


if __name__ == "__main__":
    with app.test_request_context():
        print(url_for("static", filename="style.css"))
