from flask import Blueprint, request, escape

registering = Blueprint("registering", __name__, url_prefix="/registering")


@registering.route("/")
def root() -> str:
    return f"{escape(request.url)} was called.\n"


none = Blueprint("registering", __name__)
registering.register_blueprint(none)


@none.route("/")
def index_none() -> str:
    """Nothing specified."""
    return f"{escape(request.url)} was called.\n"


when_declaring = Blueprint("when_declaring", __name__, url_prefix="/when-declaring")
registering.register_blueprint(when_declaring)


@when_declaring.route("/")
def index_when_declaring() -> str:
    """Specify the url_prefix when declaring."""
    return f"{escape(request.url)} was called.\n"


when_registering = Blueprint("when_registering", __name__)
registering.register_blueprint(when_registering, url_prefix="/when-registering")


@when_registering.route("/")
def index_when_registering() -> str:
    """Specify the url_prefix when registering."""
    return f"{escape(request.url)} was called.\n"


different = Blueprint("different", __name__, url_prefix="/different-when-declared")
registering.register_blueprint(different, url_prefix="/different-when-registered")


@different.route("/")
def index_different() -> str:
    """The url_prefix at the time of registration will be used."""
    return f"{escape(request.url)} was called.\n"
