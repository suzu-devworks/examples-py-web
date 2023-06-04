"""
Logging

server:
> flask --app src.quickstart._12_logging run --debug
"""


from flask import Flask

app = Flask(__name__)

app.logger.debug("A value for debugging")
app.logger.warning("A warning occurred (%d apples)", 42)
app.logger.error("An error occurred")
