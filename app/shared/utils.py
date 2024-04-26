from app.shared.models import db
from app.generator.models import Character
from app.account.models import User

def populate_db():
    u1 = User(id='1', name='u1', password='pass', moderator=False)
    db.session.add(u1)

    db.session.add(Character(id='1', name='c1', user=u1))
    db.session.add(Character(id='2', name='c2', user=u1))
    db.session.add(Character(id='3', name='c3', user=u1))
    db.session.commit()
