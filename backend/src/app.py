from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:secret@localhost:5432/cars"
db = SQLAlchemy(app)

from models import *

@app.route("/user", methods=['POST', 'GET'])
def request_user():
    error = False
    if request.method == 'POST':

        if request.is_json:
            data = request.get_json()
            new_user = User(
                username=data['username'], password=data['password'], role_id=data['role_id'])
            db.session.add(new_user)
            db.session.commit()
            result = [
                {
                    "message": f"User {new_user.username} has been created successfully.",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}
        else:
            error = True
            result = [
                {
                    "message": "The request payload is not in JSON format",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}

    elif request.method == 'GET':
        users = User.query.all()
        data = [
            {
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "role_id": user.role_id
            } for user in users
        ]

        result = [
            {
                "message": "Success",
                "data": data,
                "count": len(data),
                "error": error
            }
        ]

        return {"result": result}


@app.route("/role", methods=['POST', 'GET'])
def request_role():
    error = False
    if request.method == 'POST':

        if request.is_json:
            data = request.get_json()
            new_role = Role(name=data['name'])
            db.session.add(new_role)
            db.session.commit()
            result = [
                {
                    "message": f"Role {new_role.name} has been created successfully.",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}
        else:
            error = True
            result = [
                {
                    "message": "The request payload is not in JSON format",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}

    elif request.method == 'GET':
        roles = Role.query.all()
        data = [
            {
                "id": role.id,
                "name": role.name
            } for role in roles
        ]

        result = [
            {
                "message": "Success",
                "data": data,
                "count": len(data),
                "error": error
            }
        ]

        return {"result": result}


@app.route("/car", methods=['POST', 'GET'])
def request_car():
    error = False
    if request.method == 'POST':

        if request.is_json:
            data = request.get_json()
            new_car = Car(name=data['name'],
                          model=data['model'], price=data['price'])
            db.session.add(new_car)
            db.session.commit()
            result = [
                {
                    "message": f"Car {new_car.name} has been created successfully.",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}
        else:
            error = True
            result = [
                {
                    "message": "The request payload is not in JSON format",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}

    elif request.method == 'GET':
        cars = Car.query.all()
        data = [
            {
                "id": car.id,
                "name": car.name,
                "model": car.model,
                "price": car.price
            } for car in cars
        ]

        result = [
            {
                "message": "Success",
                "data": data,
                "count": len(data),
                "error": error
            }
        ]

        return {"result": result}


@app.route("/order", methods=['POST', 'GET'])
def request_order():
    error = False
    if request.method == 'POST':

        if request.is_json:
            data = request.get_json()
            new_order = Order(customer=data['customer'], date=data['date'])
            cars = data['cars']

            db.session.add(new_order)
            db.session.commit()

            for car in cars:
                new_car_order = Order_Car(
                    car=car, order=new_order.id)
                db.session.add(new_car_order)

            db.session.commit()

            result = [
                {
                    "message": f"Order {new_order.id} on {new_order.date} has been created successfully.",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}
        else:
            error = True
            result = [
                {
                    "message": "The request payload is not in JSON format",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}

    elif request.method == 'GET':
        orders = Order.query.all()
        order_cars = Order_Car.query.all()
        cars = Car.query.all()

        data = []

        for order in orders:
            ordered_cars = []
            for order_car in order_cars:
                if order.id == order_car.order:
                    for car in cars:
                        if car.id == order_car.car:
                            ordered_cars.append({
                                "id": car.id,
                                "name": car.name,
                                "model": car.model,
                                "price": car.price
                            })
            data.append({
                "id": order.id,
                "date": order.date,
                "cars": ordered_cars
            })

        result = [
            {
                "message": "Success",
                "data": data,
                "count": len(data),
                "error": error
            }
        ]

        return {"result": result}


@app.route("/ticket", methods=['POST', 'GET'])
def request_ticket():
    error = False
    if request.method == 'POST':

        if request.is_json:
            data = request.get_json()
            new_ticket = Ticket(title=data['title'],
                owner=data['owner'], customer=data['customer'], date=data['date'])
            db.session.add(new_ticket)
            db.session.commit()
            result = [
                {
                    "message": f"Ticket {new_ticket.id} on {new_ticket.date} has been created successfully.",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}
        else:
            error = True
            result = [
                {
                    "message": "The request payload is not in JSON format",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}

    elif request.method == 'GET':
        messages = Message.query.all()
        tickets = Ticket.query.all()

        data = []

        for ticket in tickets:
            message_list = []
            for message in messages:
                if ticket.id == message.ticket:
                    message_list.append({
                        "id": message.id,
                        "user": message.user,
                        "ticket": message.ticket,
                        "message": message.message,
                        "datetime": message.datetime
                    })
            
            data.append({
                "id": ticket.id,
                "title": ticket.title,
                "owner": ticket.owner,
                "customer": ticket.customer,
                "date": ticket.date,
                "messages": message_list
            })

        result = [
            {
                "message": "Success",
                "data": data,
                "count": len(data),
                "error": error
            }
        ]

        return {"result": result}


@app.route("/message", methods=['POST'])
def request_message():
    error = False
    if request.method == 'POST':

        if request.is_json:
            data = request.get_json()
            new_message = Message(user=data['user'],
                ticket=data['ticket'], message=data['message'])
            db.session.add(new_message)
            db.session.commit()
            result = [
                {
                    "message": f"Message {new_message.id} has been created successfully.",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}
        else:
            error = True
            result = [
                {
                    "message": "The request payload is not in JSON format",
                    "data": [],
                    "count": 0,
                    "error": error
                }
            ]
            return {"result": result}


if __name__ == '__main__':
    app.run()
