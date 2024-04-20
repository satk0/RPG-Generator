from dotenv import load_dotenv
from os import getenv

from flask import Flask

from app.shared.models import db
from app.generator.routes import generator
from app.utils import populate_db


load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = str(getenv("SQLALCHEMY_DATABASE_URI"))


with app.app_context():
    db.init_app(app)

    app.register_blueprint(generator)

    db.drop_all()
    db.create_all()

    populate_db()

