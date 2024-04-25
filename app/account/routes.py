from flask import Blueprint
from app.account.login import (
            login
        )

account = Blueprint("account", __name__)

@account.route('/login')
def index():
    return login()

