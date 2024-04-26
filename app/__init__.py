from dotenv import load_dotenv
from os import getenv

from flask import Flask

from app.shared.models import db
from app.shared.utils import populate_db

from app.generator.routes import generator
from app.account.routes import account

from flask_jwt_extended import JWTManager

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = str(getenv("SQLALCHEMY_DATABASE_URI"))
app.config["JWT_SECRET_KEY"] = "super-secret"  # TODO: hide it
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_CHECK_FORM'] = True


jwt = JWTManager(app)

with app.app_context():
    db.init_app(app)

    app.register_blueprint(generator)
    app.register_blueprint(account)

    db.drop_all()
    db.create_all()

    populate_db()

