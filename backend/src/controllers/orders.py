from flask import request, abort
from app import db

import models

def create_order():
    if request.is_json:
        data = request.get_json()
        new_order = models.Order(
            customer=data['customer'], date=data['date'])
        cars = data['cars']
        db.session.add(new_order)
        db.session.commit()

        for car in cars:
            new_car_order = models.Order_Car(
                car=car, order=new_order.id)
            db.session.add(new_car_order)

        db.session.commit()

        result = [
            {
                "message": f"Order {new_order.id} on {new_order.date} has been created successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]

        return result
    else:
        abort(400)

def get_orders():
    orders = models.Order.query.all()
    order_cars = models.Order_Car.query.all()
    cars = models.Car.query.all()

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
            "error": False
        }
    ]

    return result

def get_order(id):
    order = models.Order.query.get(id)
    order_cars = models.Order_Car.query.all()
    cars = models.Car.query.all()

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
    
    data = {
        "id": order.id,
        "date": order.date,
        "cars": ordered_cars
    }

    result = [
        {
            "message": "Success",
            "data": data,
            "count": len(data),
            "error": False
        }
    ]

    return result

def delete_order(id):
    order = models.Order.query.get(id)
    order_cars = models.Order_Car.query.all()

    order_id = order.id
    order_date = order.date

    for order_car in order_cars:
        if order.id == order_car.order:
            db.session.delete(order_car)
    db.session.commit()

    db.session.delete(order)
    db.session.commit()

    result = [
        {
            "message": f"Order {order_id} on {order_date} has been deleted successfully.",
            "data": [],
            "count": 0,
            "error": False
        }
    ]
    return result