from flask import render_template, jsonify, abort
from app.generator.models import Character, Name, Skill, Attribute, Item
from app.shared.models import db

from sqlalchemy import func

from flask_jwt_extended import current_user

from datetime import datetime


def load_index():
    return render_template("generator/index.html", title="RPG Generator", user=current_user)

def remove_character(character_id):

    # TODO: restrict other users access
    ch = db.one_or_404(db.select(Character)
                        .filter_by(id=character_id))

    if (not current_user.id == ch.user.id and not current_user.moderator):
        abort(404)  

    db.session.delete(ch)
    db.session.commit()

    return jsonify({})

def show_character(character_id):

    ch = db.one_or_404(db.select(Character)
                        .filter_by(id=character_id))

    if (not current_user.id == ch.user.id and not current_user.moderator):
        abort(404)  

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

    print("character_data")
    print(character_data)
    return render_template("generator/character.html", character=character_data, title="RPG Generator",
                           user=current_user)

def generate_character():

    name = db.first_or_404(db.select(Name).order_by(func.random()))

    skills = db.session.execute(db.select(Skill).order_by(func.random()).limit(3)).scalars()
    attributes = db.session.execute(db.select(Attribute).order_by(func.random()).limit(3)).scalars()
    items = db.session.execute(db.select(Item).order_by(func.random()).limit(3)).scalars()

    skills_list = [s for s in skills]
    attributes_list = [a for a in attributes]
    items_list = [i for i in items]

    print("name")
    print(name.name)

    print(current_user.name)

    c = Character(
            timestamp=datetime.now(), name=name, user=current_user,
            skills = skills_list, attributes=attributes_list,
            items = items_list
        )

    db.session.add(c)
    db.session.commit()

    return jsonify({'id': c.id})

def regenerate_character(character_id):
    c = db.one_or_404(db.select(Character)
                        .filter_by(id=character_id))

    if (not current_user.id == c.user.id and not current_user.moderator):
        abort(404)  

    name = db.first_or_404(db.select(Name).order_by(func.random()))

    skills = db.session.execute(db.select(Skill).order_by(func.random()).limit(3)).scalars()
    attributes = db.session.execute(db.select(Attribute).order_by(func.random()).limit(3)).scalars()
    items = db.session.execute(db.select(Item).order_by(func.random()).limit(3)).scalars()

    skills_list = [s for s in skills]
    attributes_list = [a for a in attributes]
    items_list = [i for i in items]

    print("name")
    print(name.name)

    print(current_user.name)

    c.name = name
    c.skills = skills_list
    c.attributes = attributes_list
    c.items = items_list

    db.session.commit()

    return jsonify({'id': c.id})
