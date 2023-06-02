"""
Hooking in WSGI Middleware

server:
> flask --app src.quickstart._13_hooking_in_wsgi run --debug
"""


from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route("/")
def index():
    return "index"
