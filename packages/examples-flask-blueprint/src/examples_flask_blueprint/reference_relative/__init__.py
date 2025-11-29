from typing import NoReturn

from flask import Blueprint, render_template

bp = Blueprint(
    "reference_relative",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/references/relative",
)


@bp.route("/")
def index() -> str | NoReturn:
    return render_template("references/relative/index.html")


@bp.route("/about")
def about() -> str | NoReturn:
    return render_template("references/relative/about.html")
