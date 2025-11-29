from typing import NoReturn

from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

bp = Blueprint("standard", __name__, template_folder="templates", url_prefix="/standard")


@bp.context_processor
def inject_blueprint_data() -> dict[str, str]:
    return {
        "bp_name": bp.name,
        "bp_url_prefix": str(bp.url_prefix),
    }


@bp.route("/", defaults={"page": "index"})
@bp.route("/<page>")
def show(page: str) -> str | NoReturn:
    try:
        return render_template(f"pages/{page}.html")
    except TemplateNotFound:
        abort(404, f"pages/{page}.html")
