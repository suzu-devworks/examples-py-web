from typing import NoReturn

from flask import Blueprint, render_template

bp = Blueprint("reference_not_specified", __name__, url_prefix="/references/not-specified")


@bp.route("/")
def index() -> str | NoReturn:
    return render_template("references/not-specified/index.html")


@bp.route("/about")
def about() -> str | NoReturn:
    return render_template("references/not-specified/about.html")
