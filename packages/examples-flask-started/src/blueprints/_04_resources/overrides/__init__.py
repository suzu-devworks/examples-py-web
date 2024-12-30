from flask import Blueprint, render_template

bp = Blueprint(
    "overrides",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/overrides",
)


@bp.route("/")
def index() -> str:
    return render_template("overrides/index.html")
