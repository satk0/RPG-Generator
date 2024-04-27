from flask import render_template, request, redirect, url_for, make_response

from uuid import uuid4
from flask_jwt_extended import (
        create_access_token, create_refresh_token,
        set_refresh_cookies, set_access_cookies,
        verify_jwt_in_request
        )

from app.account.models import User
from app.shared.models import db



def show_login_page():
    jwt = verify_jwt_in_request(optional=True)
    if jwt:
        return redirect(url_for("generator.index"))

    return render_template("login.html", title="RPG Generator")

def login_user():
    form = request.form

    print("NAME:", form["name"])
    user = db.session.execute(db.select(User).filter_by(name=form["name"], password=form["password"])).scalar()

    if not user:
       return make_response('could not verify', 401, {'Authentication': 'login required"'})   

    print("USER:", user.name)

    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    print("ACCESS_TOKEN:", access_token, refresh_token)
    
    #return redirect(url_for("generator.characters"))
    response = make_response(redirect(url_for("generator.characters")))
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response


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
