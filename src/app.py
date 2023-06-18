from flask import Flask
from v1.blueprints.tickets import tickets_blueprint
from v1.blueprints.users import users_blueprint

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

# Register blueprints - ensure all are namespaced
app.register_blueprint(tickets_blueprint, url_prefix="/api/v1")
app.register_blueprint(users_blueprint, url_prefix="/api/v1")

