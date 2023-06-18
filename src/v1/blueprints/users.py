from flask import Blueprint

users_blueprint = Blueprint('users_blueprint', __name__)

@users_blueprint.route("/users")
def users_index():
    return "All the tickets"


@users_blueprint.route("/users/<id>")
def tickets_show(id):
    return f"The user id is: {id}"