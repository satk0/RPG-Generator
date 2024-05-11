from app.shared.models import db
from app.generator.models import Name, Skill, Attribute, Item
from app.account.models import User

from werkzeug.security import generate_password_hash

def populate_db():
    n1 = Name(name='Nazwa Bohatera pierwszego')
    n2 = Name(name='Nazwa Bohatera drugiego')
    n3 = Name(name='Nazwa Bohatera trzeciego')

    db.session.add_all([n1, n2, n3])

    for i in range(4,6):
        db.session.add(Name(name='n'+str(i)))

    u1 = User(id='1', name='admin', password=generate_password_hash('adminadmin'), moderator=True)
    u2 = User(id='2', name='user1', password=generate_password_hash('passpass11'), moderator=False)
    db.session.add_all([u1, u2])

    a1 = Attribute(name='Cecha pierwsza')
    a2 = Attribute(name='Cecha druga')
    a3 = Attribute(name='Cecha trzecia')

    for i in range(4,6):
        db.session.add(Attribute(name='a'+str(i)))

    db.session.add_all([a1, a2, a3])

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
    db.session.commit()
