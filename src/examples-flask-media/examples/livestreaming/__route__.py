from logging import getLogger
from pathlib import Path

from flask import Blueprint, render_template, send_from_directory
from flask_cors import CORS
from werkzeug import Response

logger = getLogger(__name__)

bp = Blueprint("livestreaming", __name__, url_prefix="/livestreaming")
bp.add_url_rule("/", endpoint="index")

CORS(bp, resources={r"*": {"origins": "*"}})


@bp.route("/")
def index() -> str:
    return render_template("livestreaming/index.html")


@bp.route("/video/<string:file_name>")
def stream(file_name: str) -> Response:
    video_dir = "/workspaces/examples-py-web/temp/hls"
    ext = Path(file_name).suffix

    response: Response
    match ext:
        case ".ts":
            contenttype = "video/MP2T"
            response = send_from_directory(directory=video_dir, path=file_name, mimetype=contenttype)
        case _:
            response = send_from_directory(directory=video_dir, path=file_name)

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response


# @bp.errorhandler(500)
# @bp.errorhandler(404)
# def _handle_api_error(ex: Any) -> None:
#     logger.error(ex)
