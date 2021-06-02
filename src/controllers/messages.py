from flask import request, abort
from app import db

import models

def create_message():
    if request.is_json:
        data = request.get_json()
        new_message = models.Message(
            user=data['user'], ticket=data['ticket'], message=data['message'])
        db.session.add(new_message)
        db.session.commit()
        result = [
            {
                "message": f"Message {new_message.id} has been added to ticket {new_message.ticket} successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]
        return result
    else:
        abort(400)

def get_message(id):
    message = models.Message.query.get(id)
    data = {
        "id": message.id,
        "user": message.user,
        "ticket": message.ticket,
        "message": message.message,
        "datetime": message.datetime
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