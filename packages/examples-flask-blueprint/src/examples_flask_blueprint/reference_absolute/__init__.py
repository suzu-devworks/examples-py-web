from typing import NoReturn

from flask import Blueprint, render_template

bp = Blueprint(
    "reference_absolute",
    __name__,
    static_folder="/static",
    template_folder="/templates",
    url_prefix="/references/absolute",
)


@bp.route("/")
def index() -> str | NoReturn:
    return render_template("references/absolute/index.html")


@bp.route("/about")
def about() -> str | NoReturn:
    return render_template("references/absolute/about.html")
