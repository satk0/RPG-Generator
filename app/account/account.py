from flask import render_template, request, redirect, url_for, make_response, jsonify, abort

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

    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    
    #return redirect(url_for("generator.characters"))
    response = make_response(redirect(url_for("generator.index")))
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response

def logout_user():
    resp = make_response(redirect(url_for("account.render_login")))
    unset_jwt_cookies(resp)

    return resp

def show_register_page():
    jwt = verify_jwt_in_request(optional=True)
    if jwt:
        return redirect(url_for("generator.index"))

    return render_template("register.html", title="RPG Generator")

def register_user():
    form = request.form
    print(form["password"])

    new_user = User(id=str(uuid4()), name=form['name'], password=form["password"], moderator=False)
    db.session.add(new_user) 
    db.session.commit()

    #return form
    return redirect(url_for("account.render_login"))

def show_characters(user_id):
    if (not current_user.id == user_id and not current_user.moderator):
        print("LOL", current_user.id)
        abort(404)  

    characters = db.session.execute(db.select(Character)
                                        .join(User)
                                        .filter_by(id=user_id)
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

    #character = db.session.execute(db.select(Character).join(Name).filter_by(name='n3')).scalar()
    print("show characters")
    #character = db.session.execute(db.select(Character).filter_by(id=1)).scalar()

    #return jsonify({'characters': result})
    return render_template("characters.html", characters=enumerate(result), title="RPG Generator",
                           user=current_user)
