from dotenv import load_dotenv
from os import getenv

from flask import Flask

from app.shared.models import db
from app.shared.utils import populate_db

from app.generator.routes import generator
from app.account.routes import account
from app.account.models import User

from flask_jwt_extended import JWTManager

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = str(getenv("SQLALCHEMY_DATABASE_URI"))
app.config["JWT_SECRET_KEY"] = "super-secret"  # TODO: hide it
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_CHECK_FORM'] = True


jwt = JWTManager(app)

# register function to create JWT from User object
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return db.session.execute(db.select(User).filter_by(id=identity)).scalar()

with app.app_context():
    db.init_app(app)

    app.register_blueprint(generator)
    app.register_blueprint(account)

    db.drop_all()
    db.create_all()

    populate_db()

