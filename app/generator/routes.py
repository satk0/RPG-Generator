from flask import Blueprint
from app.generator.characters import (
        get_users, load_index, generate_character,
        show_character, remove_character
        )

from flask_jwt_extended import jwt_required

generator = Blueprint("generator", __name__)

@generator.route('/', methods=["GET"])
@jwt_required()
def index():
    return load_index()

@generator.route('/', methods=["POST"])
@jwt_required()
def post_index():
    return generate_character()

@generator.route('/character/<int:character_id>', methods=["GET"])
@jwt_required()
def character(character_id):
    return show_character(character_id)

@generator.route('/character/<int:character_id>', methods=["DELETE"])
@jwt_required()
def delete_character(character_id):
    return remove_character(character_id)

@generator.route('/user')
def get_user():
    return get_users()
