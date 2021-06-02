from flask import request, abort
from app import db

import models

def create_role():
    if request.is_json:
        data = request.get_json()
        new_role = models.Role(
            name=data['name'])
        db.session.add(new_role)
        db.session.commit()
        result = [
            {
                "message": f"Role {new_role.name} has been created successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]
        return result
    else:
        abort(400)

def get_roles():
    roles = models.Role.query.all()
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
            "error": False
        }
    ]
    
    return result

def get_role(id):
    role = models.Role.query.get(id)
    data = {
        "id": role.id,
        "name": role.name
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

def edit_role(id):
    if request.is_json:
        role = models.Role.query.get(id)
        data = request.get_json()
        role.name = data['name'] 
        db.session.commit()

        result = [
            {
                "message": f"Role {role.name} has been edited successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]
        return result
    else:
        abort(400)

def delete_role(id):
    role = models.Role.query.get(id)
    role_name = role.name
    db.session.delete(role)
    db.session.commit()

    result = [
        {
            "message": f"Role {role_name} has been deleted successfully.",
            "data": [],
            "count": 0,
            "error": False
        }
    ]
    return result