from flask import Blueprint, render_template

bp = Blueprint("admin", __name__, static_folder="static", template_folder="templates", url_prefix="/admin")


@bp.route("/")
def index() -> str:
    return render_template("building_urls/admin/index.html")


@bp.route("/about")
def about() -> str:
    return render_template("building_urls/admin/about.html")