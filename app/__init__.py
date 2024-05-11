from dotenv import load_dotenv
from os import getenv

from datetime import datetime
from datetime import timedelta
from datetime import timezone

from flask import Flask, url_for, redirect, make_response, abort

from app.shared.models import db
from app.shared.utils import populate_db

from app.generator.routes import generator
from app.account.routes import account
from app.account.models import User

from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, get_jwt, set_access_cookies, set_refresh_cookies, current_user, unset_jwt_cookies


load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = str(getenv("SQLALCHEMY_DATABASE_URI"))
app.config["JWT_SECRET_KEY"] = "super-secret"  # TODO: hide it
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_CHECK_FORM'] = True
app.config['JWT_TOKEN_LOCATION'] = ['cookies']

jwt = JWTManager(app)

# register function to create JWT from User object
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return db.session.execute(db.select(User).filter_by(id=identity)).scalar()

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    resp = make_response(redirect(url_for("account.login")))
    unset_jwt_cookies(resp)
    return resp

@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(redirect(url_for("account.login")))
    return resp

@jwt.unauthorized_loader
def unauthorized_token_callback(jwt_why):
    resp = make_response(redirect(url_for("account.login")))
    return resp

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
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

