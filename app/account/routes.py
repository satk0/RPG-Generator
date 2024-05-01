from flask import Blueprint, jsonify
from app.account.account import (
            show_login_page, login_user,
            register_user, show_register_page,
            logout_user
        )
from app.account.models import User
from flask_jwt_extended import jwt_required


account = Blueprint("account", __name__)

@account.route('/login', methods=['GET'])
def render_login():
    return show_login_page()

@account.route('/login', methods=['POST'])
def login():
    return login_user()

@account.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return logout_user()

@account.route('/register', methods=['GET'])
def render_register():
    return show_register_page()

@account.route('/register', methods=['POST'])
def register():
    return register_user()

@account.route('/users')
def show_users():

    users = User.query.all()
    result = []  
    for user in users:  
        user_data = {}  
        user_data['public_id'] = user.id 
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['moderator'] = user.moderator
     
        result.append(user_data)  

    return jsonify({'users': result})
