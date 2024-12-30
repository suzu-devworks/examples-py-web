from flask import Blueprint, render_template

parent = Blueprint("parent", __name__, template_folder="templates", url_prefix="/parent")
child = Blueprint("child", __name__, template_folder="templates", url_prefix="/child")
parent.register_blueprint(child)


@parent.route("/")
def show_parent() -> str:
    return render_template("parent.html")


@child.route("/")
def show_child() -> str:
    return render_template("child.html")
