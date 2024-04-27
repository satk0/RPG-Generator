from dotenv import load_dotenv
from os import getenv

from datetime import datetime
from datetime import timedelta
from datetime import timezone

from flask import Flask

from app.shared.models import db
from app.shared.utils import populate_db

from app.generator.routes import generator
from app.account.routes import account
from app.account.models import User

from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, get_jwt_identity, get_jwt, set_access_cookies, set_refresh_cookies, current_user



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

@app.after_request
def refresh_expiring_jwts(response):
    print("lol")
    try:
        print('test')
        exp_timestamp = get_jwt()["exp"]
        print('test2')
        print(exp_timestamp)
        print(current_user.id)
        print('test3')
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=current_user)
            refresh_token = create_refresh_token(identity=current_user)

            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response


with app.app_context():
    db.init_app(app)

    app.register_blueprint(generator)
    app.register_blueprint(account)

    db.drop_all()
    db.create_all()

    populate_db()

