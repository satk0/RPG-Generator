from app.shared.models import db
from app.generator.models import Character, Name, Skill, Attribute, Item
from app.account.models import User

from datetime import datetime
from datetime import timezone as tz

def populate_db():
    n1 = Name(name='Nazwa Bohatera pierwszego')
    n2 = Name(name='Nazwa Bohatera drugiego')
    n3 = Name(name='Nazwa Bohatera trzeciego')

    db.session.add_all([n1, n2, n3])

    for i in range(4,6):
        db.session.add(Name(name='n'+str(i)))

    u1 = User(id='1', name='u1', password='pass', moderator=False)
    db.session.add(u1)

    #for i in range(1,6):
    #    db.session.add(Skill(id=str(i), name='s' + str(i)))

    a1 = Attribute(name='Cecha pierwsza')
    a2 = Attribute(name='Cecha druga')
    a3 = Attribute(name='Cecha trzecia')

    for i in range(4,6):
        db.session.add(Attribute(name='a'+str(i)))

    db.session.add_all([a1, a2, a3])
    #for i in range(1,6):
    #    db.session.add(Attribute(id=str(i), name='a' + str(i)))

    s1 = Skill(name='Umiejętność pierwsza')
    s2 = Skill(name='Umiejętność druga')
    s3 = Skill(name='Umiejętność trzecia')

    for i in range(4,6):
        db.session.add(Skill(name='s'+str(i)))

    db.session.add_all([s1, s2, s3])

    i1 = Item(name='Przedmiot pierwszy')
    i2 = Item(name='Przedmiot drugi')
    i3 = Item(name='Przedmiot trzeci')

    for i in range(4,6):
        db.session.add(Item(name='i'+str(i)))

    db.session.add_all([i1, i2, i3])

    #for i in range(1,6):
    #    db.session.add(Item(id=str(i), name='i' + str(i)))
    #c1 = Character(timestamp=datetime.now(tz.utc), name=n2, user=u1)
    #c1.attributes = [a1, a2]

    #c2 = Character(timestamp=datetime.now(tz.utc), name=n3, user=u1)
    #c2.attributes = [a1, a3]
    #c2.skills = [s1, s3]
    #c2.items = [i1, i3]

    #db.session.add(c1)
    #db.session.add(c2)
    #db.session.add(Character(timestamp=datetime.now(tz.utc), name=n1, user=u1))
    #db.session.add(Character(timestamp=datetime.now(tz.utc), name=n1, user=u1))
    db.session.commit()
