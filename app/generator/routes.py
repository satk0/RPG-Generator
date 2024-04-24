from flask import Blueprint, render_template, url_for

from app.generator.characters import (
        get_characters, get_users, load_index, mod, rm_user
        )

generator = Blueprint("generator", __name__)

@generator.route('/')
def index():
    return load_index()

@generator.route('/characters/', methods=["GET","POST"])
def characters():
    return get_characters()

@generator.route('/user/')
def get_user():
    return get_users()

@generator.route('/moderacja/')
def moderacja():
    return mod()

@generator.route('/remove_user')
def remove_user():
    print(id)
    return rm_user(idn=id)
