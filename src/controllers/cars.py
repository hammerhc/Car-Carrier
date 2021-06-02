from flask import request, abort
from app import db

import models

def create_car():
    if request.is_json:
        data = request.get_json()
        new_car = models.Car(
            name=data['name'], model=data['model'], price=data['price'])
        db.session.add(new_car)
        db.session.commit()
        result = [
            {
                "message": f"Car {new_car.name} has been created successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]
        return result
    else:
        abort(400)

def get_cars():
    cars = models.Car.query.all()
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
            "error": False
        }
    ]
    
    return result

def get_car(id):
    car = models.Car.query.get(id)
    data = {
        "id": car.id,
        "name": car.name,
        "model": car.model,
        "price": car.price
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

def edit_car(id):
    if request.is_json:
        car = models.Car.query.get(id)
        data = request.get_json()
        car.name = data['name']
        car.model = data['model']
        car.price = data['price']   
        db.session.commit()

        result = [
            {
                "message": f"Car {car.name} has been edited successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]
        return result
    else:
        abort(400)

def delete_car(id):
    car = models.Car.query.get(id)
    car_name = car.name
    db.session.delete(car)
    db.session.commit()

    result = [
        {
            "message": f"Car {car_name} has been deleted successfully.",
            "data": [],
            "count": 0,
            "error": False
        }
    ]
    return result