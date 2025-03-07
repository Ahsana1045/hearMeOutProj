from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import User, Character

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()

#GET Characters owned by user
@user_routes.route('/<int:id>/characters')
@login_required
def get_user_characters(id):
    if id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403  # Prevent access to other users' data

    user_characters = Character.query.filter_by(user_id=id).all()
    return jsonify([character.to_dict() for character in user_characters])
