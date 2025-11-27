"""Logging.

References:
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#logging

Examples:
    Starting the server::

        $ flask --app examples_flask_quickstart._12_logging run --debug

    Output console::

        [2025-11-27 15:07:26,810] DEBUG in _12_logging: A value for debugging
        [2025-11-27 15:07:26,810] WARNING in _12_logging: A warning occurred (42 apples)
        [2025-11-27 15:07:26,810] ERROR in _12_logging: An error occurred

"""

from flask import Flask

app = Flask(__name__)

app.logger.debug("A value for debugging")
app.logger.warning("A warning occurred (%d apples)", 42)
app.logger.error("An error occurred")
