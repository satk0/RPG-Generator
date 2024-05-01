from flask import render_template, redirect, url_for, jsonify
from app.generator.models import Character, Name, Skill, Attribute, Item
from app.account.models import User
from app.shared.models import db

from sqlalchemy import func

from flask_jwt_extended import verify_jwt_in_request, current_user

from datetime import datetime
from datetime import timezone as tz


def load_index():
    return render_template("index.html", title="RPG Generator", username=current_user.name)

def show_characters():
    characters = db.session.execute(db.select(Character)
                                        .join(User)
                                        .filter_by(id=current_user.id)).scalars()
    result = []  
    for ch in characters:  
        character_data = {}  
        character_data['id'] = ch.id 
        character_data['timestamp'] = ch.timestamp 
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

    return jsonify({'characters': result})
    #return render_template("characters.html", characters=characters, title="RPG Generator",
    #                       username=current_user.name)

def show_character(character_id):

    ch = db.one_or_404(db.select(Character)
                        .filter_by(id=character_id)
                        .join(User)
                        .filter_by(id=current_user.id))
    character_data = {}  
    character_data['id'] = ch.id 
    character_data['timestamp'] = ch.timestamp 
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

    return jsonify(character_data)

def generate_character():

    name = db.first_or_404(db.select(Name).order_by(func.random()))

    skills = db.session.execute(db.select(Skill).order_by(func.random()).limit(3)).scalars()
    attributes = db.session.execute(db.select(Attribute).order_by(func.random()).limit(3)).scalars()
    items = db.session.execute(db.select(Item).order_by(func.random()).limit(3)).scalars()

    skills_list = [s for s in skills]
    attributes_list = [a for a in attributes]
    items_list = [i for i in items]

    if not name: return
    print("name")
    print(name.name)

    print(current_user.name)
    #print("skills:")
    #print(skills)

    c = Character(
            timestamp=datetime.now(tz.utc), name=name, user=current_user,
            skills = skills_list, attributes=attributes_list,
            items = items_list
        )
    print("character")
    print(c)
    #c.skills = skills

    print("test add")
    db.session.add(c)
    print("test commit")
    db.session.commit()
    #c2.attributes = [a1, a3]
    #c2.skills = [s1, s3]
    #c2.items = [i1, i3]

    result = []  
    for s in skills:  
        skill_data = {}  
        skill_data['id'] = s.id 
        skill_data['name'] = s.name

        result.append(skill_data)  

    print("Generated skills:")
    print(result)

    #return make_response(jsonify({'should': "generate"}))
    return jsonify({'id': c.id})

def get_users():
    return render_template("user.html", title="RPG Generator")
