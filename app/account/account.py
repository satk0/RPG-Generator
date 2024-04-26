from flask import render_template, request, redirect, url_for, make_response

from uuid import uuid4
from flask_jwt_extended import create_access_token

from app.account.models import User
from app.shared.models import db


def show_login_page():
    return render_template("login.html", title="RPG Generator")

def login_user():
    auth = request.authorization
    if not auth or not auth.name or not auth.password: 
       return make_response('could not verify', 401, {'Authentication': 'login required"'})   
    user = User.query.filter_by(name=auth.name).first()

    if not user:
        return

    access_token = create_access_token(identity=user.name)
    print("ACCESS_TOKEN:", access_token)

    
    return redirect(url_for("generator.characters"))

def show_register_page():
    return render_template("register.html", title="RPG Generator")

def register_user():
    form = request.form
    print(form["password"])

    new_user = User(id=str(uuid4()), name=form['name'], password=form["password"], moderator=False)
    db.session.add(new_user) 
    db.session.commit()

    #return form
    return redirect(url_for("account.render_login"))
