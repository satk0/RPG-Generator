from flask import Blueprint
from app.generator.characters import (
        get_characters, get_users, load_index, generate_character
        )

from flask_jwt_extended import jwt_required

generator = Blueprint("generator", __name__)

@generator.route('/', methods=["GET"])
def index():
    return load_index()

@generator.route('/', methods=["POST"])
def post_index():
    return generate_character()

@generator.route('/characters', methods=["GET"])
def get_characters():
    return get_characters()

@generator.route('/user')
def get_user():
    return get_users()
