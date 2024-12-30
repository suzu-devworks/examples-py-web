from flask import Blueprint, redirect, url_for
from werkzeug import Response

from .admin import bp as admin

bp = Blueprint(
    "building_urls",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/building-urls",
)
bp.register_blueprint(admin)


@bp.route("/")
def index() -> Response:
    return redirect(url_for("building_urls.admin.index"))
