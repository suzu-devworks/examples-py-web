from typing import NoReturn

from flask import Blueprint, render_template

from .children import bp as children

bp = Blueprint("parent", __name__, static_folder="static", template_folder="templates", url_prefix="/parent")
bp.register_blueprint(children, url_prefix="/children")


@bp.route("/")
def index() -> str | NoReturn:
    return render_template("parent/index.html")
