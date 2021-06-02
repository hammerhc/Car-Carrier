from flask import request, abort
from app import db

import models

def create_ticket():
    if request.is_json:
        data = request.get_json()
        new_ticket = models.Ticket(
            title=data['title'], owner=data['owner'], customer=data['customer'], state=data['state'])
        db.session.add(new_ticket)
        db.session.commit()
        result = [
            {
                "message": f"Ticket {new_ticket.title} has been created successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]
        return result
    else:
        abort(400)

def get_tickets():
    tickets = models.Ticket.query.all()
    data = [
        {
            "id": ticket.id,
            "title": ticket.title,
            "owner": ticket.owner,
            "customer": ticket.customer,
            "state": ticket.state,
            "date": ticket.date
        } for ticket in tickets
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

def get_ticket(id):
    ticket = models.Ticket.query.get(id)
    data = {
        "id": ticket.id,
        "title": ticket.title,
        "owner": ticket.owner,
        "customer": ticket.customer,
        "state": ticket.state,
        "date": ticket.date
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

def edit_ticket(id):
    if request.is_json:
        ticket = models.Ticket.query.get(id)
        data = request.get_json()
        ticket.title = data['title']
        ticket.owner = data['owner']
        ticket.price = data['price']   
        ticket.customer = data['customer']
        ticket.state = data['state']
        db.session.commit()

        result = [
            {
                "message": f"Ticket {ticket.title} has been edited successfully.",
                "data": [],
                "count": 0,
                "error": False
            }
        ]
        return result
    else:
        abort(400)

def delete_ticket(id):
    ticket = models.Ticket.query.get(id)
    ticket_title = ticket.title
    db.session.delete(ticket)
    db.session.commit()

    result = [
        {
            "message": f"Ticket {ticket_title} has been deleted successfully.",
            "data": [],
            "count": 0,
            "error": False
        }
    ]
    return result