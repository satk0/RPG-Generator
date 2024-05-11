from flask import render_template, redirect, url_for, make_response, abort

from uuid import uuid4
from flask_jwt_extended import (
        create_access_token, create_refresh_token,
        set_refresh_cookies, set_access_cookies,
        verify_jwt_in_request, unset_jwt_cookies,
        current_user
        )

from app.account.models import User
from app.generator.models import Character
from app.shared.models import db

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Regexp

from werkzeug.security import generate_password_hash, check_password_hash


def check_username_exist(form, field):
    user = db.session.execute(db.select(User).filter_by(name=field.data)).scalar()
    if user:
        raise ValidationError("Nazwa użytkownika już istnieje")


class RegisterForm(FlaskForm):
    # autofocus: https://stackoverflow.com/a/47839747/17342313
    name = StringField("Nazwa użytkownika",
                       validators=[DataRequired(message="Nazwa użytkownika jest wymagana"),
                                   Length(min=4, max=20), check_username_exist],
                       render_kw={'autofocus': True})
    password = PasswordField("Hasło", validators=[DataRequired(message="Nie wprowadzono hasła"),
                                                 Length(min=10, max=50),
                                                 Regexp('(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\\W)',
                                                        message="Hasło powinno składać się z małych i dużych liter, cyfr oraz znaków specjalnych")])

def register_page():
    jwt = verify_jwt_in_request(optional=True)
    if jwt:
        return redirect(url_for("generator.index"))

    form = RegisterForm()
    print(form.errors)

    if form.validate_on_submit():
        new_user = User(id=str(uuid4()), name=form.name.data, password=generate_password_hash(form.password.data), moderator=False)
        db.session.add(new_user) 
        db.session.commit()

        return redirect(url_for("account.login"))

    return render_template("account/register.html", title="RPG Generator", form=form)

class LoginForm(FlaskForm):
    name = StringField("Nazwa użytkownika",
                       validators=[DataRequired(message="Nazwa użytkownika jest wymagana"),
                                   Length(min=4, max=20)],
                       render_kw={'autofocus': True})
    password = PasswordField("Hasło", validators=[DataRequired(message="Nie wprowadzono hasła"),
                                                 Length(min=10, max=50)])

def login_page():
    jwt = verify_jwt_in_request(optional=True)
    if jwt:
        return redirect(url_for("generator.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).filter_by(name=form.name.data)).scalar()
        if not user:
           # https://techmonger.github.io/64/wtf-custom-validation-hack/
           form.password.errors.append("Błędny login lub hasło")
           return render_template("account/login.html", title="RPG Generator", form=form)

        if not check_password_hash(user.password, form.password.data):
           form.password.errors.append("Błędny login lub hasło")
           return render_template("account/login.html", title="RPG Generator", form=form)

        access_token = create_access_token(identity=user)
        refresh_token = create_refresh_token(identity=user)
        
        response = make_response(redirect(url_for("generator.index")))
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return response

    return render_template("account/login.html", title="RPG Generator", form=form)

def logout_user():
    resp = make_response(redirect(url_for("account.login")))
    unset_jwt_cookies(resp)

    return resp


def show_users():
    if (not current_user.moderator):
        abort(404)  

    users = db.session.execute(db.select(User)
                                        .order_by(User.name.asc())
                               ).scalars()

    result = []  
    for u in users:  
        u_data = {}  
        u_data['id'] = u.id 
        u_data['name'] = u.name
     
        result.append(u_data)  

    return render_template("account/users.html", users=result, title="RPG Generator",
                           user=current_user)

def show_user(user_id):
    if (not current_user.id == user_id and not current_user.moderator):
        abort(404)  

    shown_user = db.one_or_404(db.select(User).filter_by(id=user_id))

    characters = db.session.execute(db.select(Character)
                                        .join(User)
                                        .filter_by(id=user_id)
                                        .order_by(Character.timestamp.desc())
                                    ).scalars()
    result = []  
    for ch in characters:  
        character_data = {}  
        character_data['id'] = ch.id 
        character_data['timestamp'] = ch.timestamp.strftime("%d.%m.%Y %H:%M:%S")
        character_data['name'] = ch.name.name 
        character_data['uid'] = ch.user.id

        skill_list = [s.name for s in ch.skills]
        print("skill list:")
        print(skill_list)
        character_data['skills'] = skill_list

        attributes_list = [a.name for a in ch.attributes]
        print("attributes list:")
        print(attributes_list)
        character_data['attributes'] = attributes_list

        items_list = [i.name for i in ch.items]
        print("items list:")
        print(items_list)
        character_data['items'] = items_list
     
        result.append(character_data)  

    return render_template("account/characters.html", characters=enumerate(result), title="RPG Generator",
                           user=current_user, shown_user=shown_user)
