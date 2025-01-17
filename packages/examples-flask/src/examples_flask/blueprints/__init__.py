from flask import Blueprint, render_template

from .encodings import bp as encodings
from .overriding import bp as overriding

bp = Blueprint(
    "blueprints",
    __name__,
    template_folder="templates",
)

bp.register_blueprint(overriding, url_prefix="/overriding")
bp.register_blueprint(encodings, url_prefix="/encodings")


@bp.route("/")
def index() -> str:
    return render_template("blueprints/index.html")
