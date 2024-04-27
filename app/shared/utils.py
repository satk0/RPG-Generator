from app.shared.models import db
from app.generator.models import Character, Name, Skill, Attribute, Item
from app.account.models import User

from datetime import datetime
from datetime import timezone as tz

def populate_db():
    n1 = Name(id='1', name='n1')
    n2 = Name(id='2', name='n2')
    n3 = Name(id='3', name='n3')

    db.session.add(n1)
    db.session.add(n2)
    db.session.add(n3)

    for i in range(4,6):
        db.session.add(Name(id=str(i), name='n'+str(i)))

    u1 = User(id='1', name='u1', password='pass', moderator=False)
    db.session.add(u1)

    #for i in range(1,6):
    #    db.session.add(Skill(id=str(i), name='s' + str(i)))

    a1 = Attribute(id=1, name='a1')
    a2 = Attribute(id=2, name='a2')
    a3 = Attribute(id=3, name='a3')
    #for i in range(1,6):
    #    db.session.add(Attribute(id=str(i), name='a' + str(i)))


    #for i in range(1,6):
    #    db.session.add(Item(id=str(i), name='i' + str(i)))
    c1 = Character(id='1', timestamp=datetime.now(tz.utc), name=n2, user=u1)
    c1.attributes = [a1, a2]

    c2 = Character(id='2', timestamp=datetime.now(tz.utc), name=n3, user=u1)
    c2.attributes = [a1, a3]

    db.session.add(c1)
    db.session.add(c2)
    db.session.add(Character(id='3', timestamp=datetime.now(tz.utc), name=n1, user=u1))
    db.session.add(Character(id='4', timestamp=datetime.now(tz.utc), name=n1, user=u1))
    db.session.commit()
