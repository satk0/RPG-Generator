from flask import render_template, url_for, redirect
from app.characters.models import Character
from app.shared.models import db

lol = {
    "id": 1
    }

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
def mod():
    characters = db.session.execute(db.select(Character)).scalars()
    print(characters)
    return render_template("mod.html",characters=characters, title="Moderacja")

def add_user():
    #db.session.add(Character(id='1', name='c1'))
    return None

def rm_user(idn):
    print("wykonianienienaienae")
   # db.session.execute(db.delete(Character).where(Character.id == idn))
    character = db.session.query(Character).filter(Character.id == idn).one_or_none()
    if character:
        db.session.delete(character)
        db.session.commit()
        print("ISTNIEJE")

    return redirect(url_for('generator.moderacja'))

    
