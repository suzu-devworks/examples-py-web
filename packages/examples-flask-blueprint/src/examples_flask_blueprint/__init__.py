from typing import Any, Mapping

from flask import Flask, render_template


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    from .nested import bp as bp_nested
    from .override import bp as bp_override
    from .reference_absolute import bp as bp_reference_absolute
    from .reference_not_specified import bp as bp_reference_not_specified
    from .reference_relative import bp as bp_reference_relative
    from .standard import bp as bp_standard

    app.register_blueprint(bp_standard)
    app.register_blueprint(bp_override, url_prefix="/override-alias")
    app.register_blueprint(bp_reference_absolute)
    app.register_blueprint(bp_reference_not_specified)
    app.register_blueprint(bp_reference_relative)
    app.register_blueprint(bp_nested)

    @app.route("/")
    def index() -> str:
        return render_template("index.html")

    return app
