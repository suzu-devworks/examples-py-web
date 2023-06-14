import time

from examples.livecv.live_camera import VideoCamera
from flask import Blueprint, Response, render_template

bp = Blueprint("livecv", __name__, url_prefix="/livecv")
bp.add_url_rule("/", endpoint="index")


def gen(camera):
    while True:
        frame = camera.get_frame()
        # yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
        time.sleep(1 / 30)


@bp.route("/")
def index() -> str:
    return render_template("livecv/index.html")


@bp.route("/video_feed")
def video_feed() -> Response:
    # camera = VideoCamera("/workspaces/examples-py-web/src/temp/input.mp4")
    camera = VideoCamera("udp://0.0.0.0:5501")
    # camera = VideoCamera("srt://0.0.0.0:5501?mode=listener")
    return Response(gen(camera), mimetype="multipart/x-mixed-replace; boundary=frame")
