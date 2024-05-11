from flask import Blueprint
from app.account.account import (
            show_login_page, login_user,
            register_user, show_register_page,
            logout_user, show_user,
            show_users
        )

from flask_jwt_extended import jwt_required


account = Blueprint("account", __name__)

@account.route('/login', methods=['GET'])
def get_login():
    return show_login_page()

@account.route('/login', methods=['POST'])
def post_login():
    return login_user()

@account.route('/logout', methods=['POST'])
def logout():
    return logout_user()

@account.route('/register', methods=['GET', 'POST'])
def register():
    return show_register_page()

#@account.route('/register', methods=['POST'])
#def post_register():
#    return register_user()

@account.route('/user/<user_id>', methods=["GET"])
@jwt_required()
def get_user(user_id: str):
    return show_user(user_id)

@account.route('/users', methods=["GET"])
@jwt_required()
def get_users():
    return show_users()
