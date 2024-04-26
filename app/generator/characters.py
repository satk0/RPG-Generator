from flask import render_template
from app.generator.models import Character
from app.shared.models import db

def load_index():
    return render_template("index.html", title="RPG Generator")

def get_characters():
    # TODO: Actually use arguments

    characters = db.session.execute(db.select(Character)).scalars()
    print(characters)
    return render_template("characters.html", characters=characters, title="RPG Generator")

def get_users():
    # TODO: Actually use arguments
    #characters = Character.filter(1==1).all()
    return render_template("user.html", title="RPG Generator")
