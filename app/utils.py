from app.shared.models import db
from app.characters.models import Character

def populate_db():
    db.session.add(Character(id='1', name='c1'))
    db.session.add(Character(id='2', name='c2'))
    db.session.add(Character(id='3', name='c3'))
    db.session.commit()
