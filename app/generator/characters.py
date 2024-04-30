from flask import render_template, redirect, url_for, jsonify, make_response
from app.generator.models import Character, Name, Skill
from app.shared.models import db

from sqlalchemy import func

from flask_jwt_extended import verify_jwt_in_request, current_user


def load_index():
    jwt = verify_jwt_in_request(optional=True)
    if not jwt:
        return redirect(url_for("account.login"))

    return render_template("index.html", title="RPG Generator", username=current_user.name)

def show_characters():
    jwt = verify_jwt_in_request(optional=True)
    if not jwt:
        return redirect(url_for("account.login"))

    characters = db.session.execute(db.select(Character)).scalars()
    result = []  
    for ch in characters:  
        character_data = {}  
        character_data['id'] = ch.id 
        character_data['timestamp'] = ch.timestamp 
        character_data['name'] = ch.name.name 
     
        result.append(character_data)  

    character = db.session.execute(db.select(Character).join(Name).filter_by(name='n3')).scalar()

    if not character:
        return 

    print(character.timestamp)
    print(character.attributes)

    print("Attributes:")
    for a in character.attributes:
        print(a.name)

    print("Skills:")
    for s in character.skills:
        print(s.name)

    print("Items:")
    for i in character.items:
        print(i.name)

    return jsonify({'characters': result})
    #return render_template("characters.html", characters=characters, title="RPG Generator",
    #                       username=current_user.name)

def generate_character():
    #jwt = verify_jwt_in_request(optional=True)
    #if not jwt:
    #    return redirect(url_for("account.login"))

    skills = db.session.execute(db.select(Skill).order_by(func.random()).limit(3)).scalars()

    result = []  
    for s in skills:  
        skill_data = {}  
        skill_data['id'] = s.id 
        skill_data['name'] = s.name

        result.append(skill_data)  

    print("Generated skills:")
    print(result)

    #return make_response(jsonify({'should': "generate"}))
    return jsonify({'id': 1})

def get_users():
    return render_template("user.html", title="RPG Generator")
