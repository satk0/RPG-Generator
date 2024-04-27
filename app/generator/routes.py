from flask import Blueprint
from app.generator.characters import (
        get_characters, get_users, load_index
        )

from flask_jwt_extended import jwt_required

generator = Blueprint("generator", __name__)

@generator.route('/')
def index():
    print("test")
    return load_index()

@generator.route('/characters', methods=["GET","POST"])
def characters():
    return get_characters()

@generator.route('/user')
def get_user():
    return get_users()
