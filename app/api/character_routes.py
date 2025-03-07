from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Character, Like
from sqlalchemy.sql import func
import random

character_routes = Blueprint('characters', __name__)

#GET ALL CHARACTERS
@character_routes.route('')
# @login_required
def get_characters():
    characters = Character.query.all()
    return jsonify([char.to_dict() for char in characters])

# GET RANDOM Character
from sqlalchemy.sql.expression import func

@character_routes.route("/random", methods=["GET"])
@login_required
def get_random_character():
    # Get all character IDs the user has liked
    liked_character_ids = db.session.query(Like.character_id).filter(Like.user_id == current_user.id)

    # Query a random character that the user hasn't liked
    random_character = (
        Character.query
        .filter(~Character.id.in_(liked_character_ids))  # Exclude liked characters
        .order_by(func.random())  # Get a random one
        .first()
    )

    if not random_character:
        return jsonify({"message": "No new characters to show"}), 404

    return jsonify(random_character.to_dict())









# @character_routes.route("/random", methods=["GET"])
# @login_required
# def get_random_character():
#     # Get all character IDs, excluding liked ones
#     liked_character_ids = {like.character_id for like in current_user.likes}

#     random_character = (
#         Character.query
#         .filter(~Character.id.in_(liked_character_ids))  # Exclude liked characters
#         .order_by(func.random())  # Get a random one
#         .first()
#     )

#     if not random_character:
#         return jsonify({"message": "No new characters to show"}), 404

#     return jsonify(random_character.to_dict())




#GET Random Character by RANDOM ID
# @character_routes.route("/random-id", methods=["GET"])
# @login_required
# def get_random_character_id():
#     character_id = db.session.query(Character.id).order_by(func.random()).limit(1).scalar()

#     if not character_id:
#         return jsonify({"message": "No characters found"}), 404

#     return jsonify({"character_id": character_id})

#Get RANDOM 3
# @character_routes.route("/random", methods=["GET"])
# @login_required
# def get_random_character():
#     # Get all character IDs, excluding liked ones
#     liked_character_ids = {like.character_id for like in current_user.likes}

#     random_character = (
#         Character.query
#         .filter(~Character.id.in_(liked_character_ids))  # Exclude liked characters
#         .order_by(func.random())  # Get a random one
#         .first()
#     )

#     if not random_character:
#         return jsonify({"message": "No new characters to show"}), 404

#     return jsonify(random_character.to_dict())





#CREATE A CHARACTER (LOGIN REQUIRED)
from sqlalchemy.exc import IntegrityError
from flask import jsonify

# CREATE A CHARACTER (LOGIN REQUIRED)
@character_routes.route('', methods=['POST'])
@login_required
def create_character():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    image_url = data.get("image_url")

    if not name or not description or not image_url:
        return jsonify({"error": "All fields are required"}), 400

    # Check if character name already exists
    existing_character = Character.query.filter_by(name=name).first()
    if existing_character:
        return jsonify({"error": "Character with this name already exists"}), 400

    new_character = Character(
        name=name,
        description=description,
        image_url=image_url,
        user_id=current_user.id  # Assigns the logged-in user as the creator
    )

    try:
        db.session.add(new_character)
        db.session.commit()
        return jsonify(new_character.to_dict()), 201
    except IntegrityError:
        db.session.rollback()  # Rollback transaction in case of failure
        return jsonify({"error": "An error occurred while creating the character"}), 500


# @character_routes.route('', methods=['POST'])
# @login_required
# def create_character():
#     data = request.get_json()
#     name = data.get("name")
#     description = data.get("description")
#     image_url = data.get("image_url")

#     if not name or not description or not image_url:
#         return jsonify({"error": "All fields are required"}), 400

#     new_character = Character(
#         name=name,
#         description=description,
#         image_url=image_url,
#         user_id=current_user.id  # Assigns the logged-in user as the creator
#     )

#     db.session.add(new_character)
#     db.session.commit()

#     return jsonify(new_character.to_dict()), 201

#UPDATE A CHARACTER (ONLY IF CREATED BY THE USER)
@character_routes.route('/<int:character_id>', methods=['PUT'])
@login_required
def update_character(character_id):
    character = Character.query.get(character_id)

    if not character:
        return jsonify({"error": "Character not found"}), 404

    if character.user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403  # Only owner can edit

    data = request.get_json()
    character.name = data.get("name", character.name)
    character.description = data.get("description", character.description)
    character.image_url = data.get("image_url", character.image_url)

    db.session.commit()
    return jsonify(character.to_dict())

#DELETE A CHARACTER (ONLY IF CREATED BY THE USER)
@character_routes.route('/<int:character_id>', methods=['DELETE'])
@login_required
def delete_character(character_id):
    character = Character.query.get(character_id)

    if not character:
        return jsonify({"error": "Character not found"}), 404

    if character.user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403  # Only owner can delete

    db.session.delete(character)
    db.session.commit()
    return jsonify({"message": "Character deleted successfully"}), 200

#GET TOP 5 MOST LIKED CHARACTERS
@character_routes.route('/top-liked')
def get_top_liked_characters():
    top_characters = (
        db.session.query(Character, func.count(Like.id).label('like_count'))
        .join(Like)
        .group_by(Character.id)
        .order_by(func.count(Like.id).desc())
        .limit(5)
        .all()
    )

    return jsonify([
        {
            "id": character.id,
            "name": character.name,
            "description": character.description,
            "image_url": character.image_url,
            "like_count": like_count
        }
        for character, like_count in top_characters
    ])
