from flask import render_template, redirect, url_for, jsonify
from app.generator.models import Character, Name
from app.shared.models import db

from flask_jwt_extended import verify_jwt_in_request, current_user


def load_index():
    jwt = verify_jwt_in_request(optional=True)
    if not jwt:
        return redirect(url_for("account.login"))

    return render_template("index.html", title="RPG Generator", username=current_user.name)

def get_characters():
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
    return jsonify({'should': "generate"})

def get_users():
    return render_template("user.html", title="RPG Generator")
