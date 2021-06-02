from flask import request, abort
import hashlib, binascii
from app import db

import models
import controllers.users as users

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def login():
    if request.is_json:
        data = request.get_json()
        all_users = models.User.query.all()
        username = data['username']
        password = data['password']
        is_valid = False

        for user in all_users:
            if user.username == username:
                is_valid = verify_password(user.password, password)

        result = []

        if is_valid:
            result = [
                {
                    "message": "Success",
                    "data": [],
                    "count": 0,
                    "error": False
                }
            ]
        
        else:
            result = [
                {
                    "message": "Wrong username or password!",
                    "data": [],
                    "count": 0,
                    "error": True
                }
            ]

        return result
    else:
        abort(400)

def register():
    if request.is_json:
        data = request.get_json()
        all_users = models.User.query.all()
        username = data['username']
        is_valid = True

        for user in all_users:
            if user.username == username:
                is_valid = False

        result = []

        if is_valid:
            result = users.create_user()
        
        else:
            result = [
                {
                    "message": "Username already used!",
                    "data": [],
                    "count": 0,
                    "error": True
                }
            ]

        return result
    else:
        abort(400)

def logout():
    pass