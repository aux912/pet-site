from flask import Blueprint
from .models import User
from .extensions import db

user = Blueprint('user', __name__) # route name definition and current file name

@user.route('user/<name>')
def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return 'User created'
