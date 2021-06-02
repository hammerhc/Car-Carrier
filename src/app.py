from flask import Flask, request, abort, render_template
from flask_sqlalchemy import SQLAlchemy
import os

""" filepath = os.path.realpath(__file__)

def uppath(path, n):
    for i in range(n):
        path = os.path.dirname(path)
    
    return path

project_path = uppath(filepath, 3)
frontend_path = os.path.join(project_path, "frontend")
templates_path = os.path.join(frontend_path, "templates")
static_path = os.path.join(frontend_path, "static") """

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:secret@localhost:5432/cars"
db = SQLAlchemy(app)

import controllers.cars as cars
import controllers.account as account
import controllers.messages as messages
import controllers.orders as orders
import controllers.roles as roles
import controllers.states as states
import controllers.tickets as tickets
import controllers.users as users


@app.errorhandler(400)
def bad_request(error):
    result = {
        "message": "{error}",
        "data": [],
        "count": 0,
        "error": True
    }

    return {"result": result}


@app.errorhandler(401)
def unauthorized(error):
    result = {
        "message": "{error}",
        "data": [],
        "count": 0,
        "error": True
    }

    return {"result": result}

@app.errorhandler(403)
def forbidden(error):
    result = {
        "message": "{error}",
        "data": [],
        "count": 0,
        "error": True
    }

    return {"result": result}


@app.errorhandler(404)
def not_found(error):
    result = {
        "message": "{error}",
        "data": [],
        "count": 0,
        "error": True
    }

    return {"result": result}

@app.errorhandler(405)
def method_not_allowed(error):
    result = {
        "message": "{error}",
        "data": [],
        "count": 0,
        "error": True
    }

    return {"result": result}

@app.errorhandler(500)
def server_error(error):
    result = {
        "message": "{error}",
        "data": [],
        "count": 0,
        "error": True
    }

    return {"result": result}

@app.route("/", methods=['GET'])
def home_page():
    return render_template("index.html")

@app.route("/cars", methods=['GET'])
def cars_page():
    return render_template("cars.html")

@app.route("/orders", methods=['GET'])
def orders_page():
    return render_template("orders.html")

@app.route("/help", methods=['GET'])
def help_page():
    return render_template("help.html")

@app.route("/admin", methods=['GET'])
def admin_page():
    return render_template("admin.html")

@app.route("/login", methods=['POST'])
def request_login():
    result = []

    if request.method == "POST":
        result = account.login()

    return {"result": result}

@app.route("/register", methods=['POST'])
def request_register():
    result = []

    if request.method == "POST":
        result = account.register()

    return {"result": result}

@app.route("/logout", methods=['POST'])
def request_logout():
    result = []

    if request.method == "POST":
        result = account.logout()

    return {"result": result}

@app.route("/user", methods=['POST', 'GET'])
def request_users():
    result = []

    if request.method == 'POST':
        result = users.create_user()

    if request.method == "GET":
        result = users.get_users()

    return {"result": result}


@app.route("/user/<id>", methods=['PUT', 'GET', 'DELETE'])
def request_user(id):
    result = []

    if request.method == "PUT":
        result = users.edit_user(id)

    if request.method == "GET":
        result = users.get_user(id)

    if request.method == "DELETE":
        result = users.delete_user(id)

    return {"result": result}


@app.route("/role", methods=['POST', 'GET'])
def request_roles():
    result = []

    if request.method == "POST":
        result = roles.create_role()

    if request.method == "GET":
        result = roles.get_roles()

    return {"result": result}


@app.route("/role/<id>", methods=['PUT', 'GET', 'DELETE'])
def request_role(id):
    result = []

    if request.method == "PUT":
        result = roles.edit_role(id)

    if request.method == "GET":
        result = roles.get_role(id)

    if request.method == "DELETE":
        result = roles.delete_role(id)

    return {"result": result}


@app.route("/car", methods=['POST', 'GET'])
def request_cars():
    result = []

    if request.method == "POST":
        result = cars.create_car()

    if request.method == "GET":
        result = cars.get_cars()

    return {"result": result}


@app.route("/car/<id>", methods=['PUT', 'GET', 'DELETE'])
def request_car(id):
    result = []

    if request.method == "PUT":
        result = cars.edit_car(id)

    if request.method == "GET":
        result = cars.get_car(id)

    if request.method == "DELETE":
        result = cars.delete_car(id)

    return {"result": result}


@app.route("/order", methods=['POST', 'GET'])
def request_orders():
    result = []

    if request.method == "POST":
        result = orders.create_order()

    if request.method == "GET":
        result = orders.get_orders()

    return {"result": result}


@app.route("/order/<id>", methods=['GET', 'DELETE'])
def request_order(id):
    result = []

    if request.method == "GET":
        result = orders.get_order(id)

    if request.method == "DELETE":
        result = orders.delete_order(id)

    return {"result": result}


@app.route("/ticket", methods=['POST', 'GET'])
def request_tickets():
    result = []

    if request.method == "POST":
        result = tickets.create_ticket()

    if request.method == "GET":
        result = tickets.get_tickets()

    return {"result": result}


@app.route("/ticket/<id>", methods=['PUT', 'GET', 'DELETE'])
def request_ticket(id):
    result = []

    if request.method == "PUT":
        result = tickets.edit_ticket(id)

    if request.method == "GET":
        result = tickets.get_ticket(id)

    if request.method == "DELETE":
        result = tickets.delete_ticket(id)

    return {"result": result}

@app.route("/state", methods=['POST', 'GET'])
def request_states():
    result = []

    if request.method == "POST":
        result = states.create_state()

    if request.method == "GET":
        result = states.get_states()

    return {"result": result}


@app.route("/state/<id>", methods=['PUT', 'GET', 'DELETE'])
def request_state(id):
    result = []

    if request.method == "PUT":
        result = states.edit_state(id)

    if request.method == "GET":
        result = states.get_state(id)

    if request.method == "DELETE":
        result = states.delete_state(id)

    return {"result": result}

@app.route("/message", methods=['POST'])
def request_messages():
    result = []

    if request.method == "POST":
        result = messages.create_message()

    return {"result": result}


@app.route("/message/<id>", methods=['GET'])
def request_message(id):
    result = []

    if request.method == "GET":
        result = messages.get_message(id)

    return {"result": result}


if __name__ == '__main__':
    app.run()
