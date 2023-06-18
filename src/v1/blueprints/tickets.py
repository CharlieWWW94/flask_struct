from flask import Blueprint

tickets_blueprint = Blueprint('tickets_blueprint', __name__)

@tickets_blueprint.route("/tickets")
def tickets_index():
    return "All the tickets"


@tickets_blueprint.route("/tickets/<id>")
def tickets_show(id):
    return f"The ticket id is: {id}"