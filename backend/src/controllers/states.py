from flask import request, abort
from app import db

import models

def create_state():
    if request.is_json:
        data = request.get_json()
        new_state = models.State(
            name=data['name'])
        db.session.add(new_state)
        db.session.commit()
        result = [
            {
                "message": f"State {new_state.name} has been created successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]
        return result
    else:
        abort(400)

def get_states():
    states = models.State.query.all()
    data = [
        {
            "id": state.id,
            "name": state.name
        } for state in states
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

def get_state(id):
    state = models.State.query.get(id)
    data = {
        "id": state.id,
        "name": state.name
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

def edit_state(id):
    if request.is_json:
        state = models.State.query.get(id)
        data = request.get_json()
        state.name = data['name']
        db.session.commit()

        result = [
            {
                "message": f"State {state.name} has been edited successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]
        return result
    else:
        abort(400)

def delete_state(id):
    state = models.State.query.get(id)
    state_name = state.name
    db.session.delete(state)
    db.session.commit()

    result = [
        {
            "message": f"State {state_name} has been deleted successfully.",
            "data": [],
            "count": 0,
            "error": False
        }
    ]
    return result