import os
from logging import getLogger

from flask import Blueprint, Response, render_template, request

from examples.videochunks.utility import parse_range_header

logger = getLogger(__name__)

bp = Blueprint("videochunks", __name__, url_prefix="/videochunks")
bp.add_url_rule("/", endpoint="index")


@bp.route("/")
def index() -> str:
    return render_template("videochunks/index.html")


@bp.after_request
def after_request(response: Response) -> Response:
    response.headers.add("Accept-Ranges", "bytes")
    return response


def get_chunk(
    file_path: str, byte1: int, byte2: int | None = None, chunk_size: int = 131072
) -> tuple[bytes, int, int, int]:
    file_size = os.stat(file_path).st_size
    start = 0

    if byte1 < file_size:
        start = byte1

    if byte2:
        length = byte2 + 1 - byte1
    elif start + chunk_size < file_size:
        length = chunk_size
    else:
        length = file_size - start

    with open(file_path, "rb") as f:
        f.seek(start)
        chunk = f.read(length)

    return chunk, start, length, file_size


@bp.route("/video_feed")
def get_file() -> Response:
    range_header = request.headers.get("Range", None)
    logger.debug(f"mp4 - Range: {range_header}")
    byte1, byte2 = parse_range_header(range_header)

    file_path = "/workspaces/examples-py-web/temp/input.mp4"
    chunk, start, length, file_size = get_chunk(file_path, byte1, byte2)

    resp = Response(chunk, 206, mimetype="video/mp4", content_type="video/mp4", direct_passthrough=True)
    resp.headers.add("Content-Range", "bytes {0}-{1}/{2}".format(start, start + length - 1, file_size))
    logger.debug(f"mp4 - Content-Range: bytes {start}-{start + length - 1}/{file_size}")

    return resp
