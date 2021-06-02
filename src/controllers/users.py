from flask import request, abort
from app import db

import models

def create_user():
    if request.is_json:
        data = request.get_json()
        new_user = models.User(
            username=data['username'], password=data['password'], role_id=data['role_id'])
        db.session.add(new_user)
        db.session.commit()
        result = [
            {
                "message": f"User {new_user.username} has been created successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]
        return result
    else:
        abort(400)

def get_users():
    users = models.User.query.all()
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
            "error": False
        }
    ]
    
    return result

def get_user(id):
    user = models.User.query.get(id)
    data = {
        "id": user.id,
        "username": user.username,
        "password": user.password,
        "role_id": user.role_id
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

def edit_user(id):
    if request.is_json:
        user = models.User.query.get(id)
        data = request.get_json()
        user.username = data['username']
        user.password = data['password']
        user.role_id = data['role_id']   
        db.session.commit()

        result = [
            {
                "message": f"User {user.username} has been edited successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]
        return result
    else:
        abort(400)

def delete_user(id):
    user = models.User.query.get(id)
    user_name = user.name
    db.session.delete(user)
    db.session.commit()

    result = [
        {
            "message": f"User {user_name} has been deleted successfully.",
            "data": [],
            "count": 0,
            "error": False
        }
    ]
    return result