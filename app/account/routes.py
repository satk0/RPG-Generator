from flask import Blueprint, jsonify
from app.account.account import (
            login, register_user, show_register_page
        )
from app.account.models import User

account = Blueprint("account", __name__)

@account.route('/login')
def render_login():
    return login()

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
