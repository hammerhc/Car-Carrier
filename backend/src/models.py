from datetime import datetime
import hashlib, binascii, os
from app import db


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    order = db.relationship('Order', backref='order_id', lazy=True)
    message = db.relationship('Message', backref='user_message_id', lazy=True)

    def __init__(self, username, password, role_id):
        self.username = username
        self.password = hash_password(password)
        self.role_id = role_id

class Role(db.Model):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    user = db.relationship('User', backref='user_id', lazy=True)

    def __init__(self, name):
        self.name = name


class Car(db.Model):
    __tablename__ = "car"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    model = db.Column(db.String(), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price


class Order_Car(db.Model):
    __tablename__ = "order_car"

    order = db.Column(db.Integer, db.ForeignKey("order.id"), primary_key=True)
    car = db.Column(db.Integer, db.ForeignKey("car.id"), primary_key=True)
    order_id = db.relationship('Order', backref='orders', lazy=True)
    car_id = db.relationship('Car', backref='cars', lazy=True)

    def __init__(self, order, car):
        self.order = order
        self.car = car


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, customer, date):
        self.customer = customer
        self.date = date


class Ticket(db.Model):
    __tablename__ = "ticket"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    customer = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    state = db.Column(db.Integer, db.ForeignKey("state.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    message = db.relationship('Message', backref='message_id', lazy=True)
    owner_id = db.relationship('User', foreign_keys=[owner], backref='ticket_owner', lazy=True)
    customer_id = db.relationship('User', foreign_keys=[customer], backref='ticket_customer', lazy=True)
    state_id = db.relationship('State', backref='ticket_state', lazy=True)

    def __init__(self, title, owner, customer, date):
        self.title = title
        self.owner = owner
        self.customer = customer
        self.date = date


class State(db.Model):
    __tablename__ = "state"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __init__ (self, name):
        self.name = name

class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey(
        "user.id"), nullable=False)
    ticket = db.Column(db.Integer, db.ForeignKey(
        "ticket.id"), nullable=False)
    message = db.Column(db.String(), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)


    def __init__(self, user, ticket, message):
        self.user = user
        self.ticket = ticket
        self.message = message
        self.datetime = datetime.now()
