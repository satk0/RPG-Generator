from flask import render_template, redirect, url_for, jsonify
from app.generator.models import Character
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
    print(characters)
    result = []  
    for ch in characters:  
        character_data = {}  
        character_data['timestamp'] = ch.timestamp 
        character_data['name'] = ch.name.name 
     
        result.append(character_data)  

    return jsonify({'characters': result})
    #return render_template("characters.html", characters=characters, title="RPG Generator",
    #                       username=current_user.name)

def get_users():
    return render_template("user.html", title="RPG Generator")
