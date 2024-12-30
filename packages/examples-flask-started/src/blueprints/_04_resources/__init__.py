from flask import Blueprint, render_template

from .admin import bp as admin
from .overrides import bp as overrides

resources = Blueprint(
    "resources", __name__, static_folder="static", template_folder="templates", url_prefix="/resources"
)
print("Blueprint Resource Folder:", resources.root_path)

with resources.open_resource("static/style.css") as f:
    code = f.read()
    print("style.css is:\n", code)

resources.register_blueprint(admin)
resources.register_blueprint(overrides)


@resources.route("/")
def index() -> str:
    return render_template("resources/index.html")
