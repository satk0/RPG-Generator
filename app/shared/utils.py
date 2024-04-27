from app.shared.models import db
from app.generator.models import Character, Name
from app.account.models import User

from datetime import datetime

from datetime import datetime
from datetime import timedelta
from datetime import timezone as tz

def populate_db():
    n1 = Name(id='1', name='n1')
    db.session.add(n1)
    u1 = User(id='1', name='u1', password='pass', moderator=False)
    db.session.add(u1)

    db.session.add(Character(timestamp=datetime.now(tz.utc), name=n1, user=u1))
    db.session.add(Character(timestamp=datetime.now(tz.utc), name=n1, user=u1))
    db.session.add(Character(timestamp=datetime.now(tz.utc), name=n1, user=u1))
    db.session.commit()
