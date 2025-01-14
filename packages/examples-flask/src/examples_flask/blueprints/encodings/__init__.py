from flask import Blueprint, current_app, render_template
from markupsafe import escape

bp = Blueprint(
    "encodings",
    __name__,
    static_folder="static",
    static_url_path="/static/encodings",
    template_folder="templates",
)


@bp.route("/")
def index() -> str:
    raw: bytes | None = None
    decoded: str | None = None
    text: str | None = None

    with bp.open_resource("resources/resource_utf8.txt") as f:
        data = f.read()
        raw = data if isinstance(data, bytes) else str(data).encode()
        current_app.logger.debug(f"raw: {str(raw)}")

        decoded = raw.decode()
        current_app.logger.debug(f"decoded: {str(decoded)}")

    with bp.open_resource("resources/resource_utf8.txt", mode="r", encoding="utf-8") as f:
        text = str(f.read())
        current_app.logger.debug(f"encoding read: {str(text)}")

    return render_template(
        "encodings/index.html",
        raw=escape(str(raw)),
        decoded=escape(decoded),
        text=escape(text),
    )
