from flask import render_template, request, redirect, url_for
from uuid import uuid4

from app.account.models import User
from app.shared.models import db


def login():
    return render_template("login.html", title="RPG Generator")

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
