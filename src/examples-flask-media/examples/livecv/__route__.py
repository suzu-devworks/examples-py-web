from typing import Any, Callable, Generator

from examples.livecv.video_camera import VideoCamera
from flask import Blueprint, Response, render_template

bp = Blueprint("livecv", __name__, url_prefix="/livecv")
bp.add_url_rule("/", endpoint="index")

# TODO blocked by video start.
# camera = VideoCamera("/workspaces/examples-py-web/temp/input.mp4")
camera: VideoCamera
camera = VideoCamera("udp://0.0.0.0:5501")


def generate(get_frame: Callable[..., Any]) -> Generator[bytes, None, None]:
    while True:
        frame = get_frame()
        if frame is None:
            print("frame is none")
            break

        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@bp.route("/")
def index() -> str:
    camera.start()
    return render_template("livecv/index.html")


@bp.route("/video_feed")
def video_feed() -> Response:
    return Response(generate(lambda: camera.get_frame()), mimetype="multipart/x-mixed-replace; boundary=frame")


@bp.route("/video_feed_gray")
def video_feed_gray() -> Response:
    return Response(generate(lambda: camera.get_gray_frame()), mimetype="multipart/x-mixed-replace; boundary=frame")
