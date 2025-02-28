from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Character, Like
from sqlalchemy.sql import func

character_routes = Blueprint('characters', __name__)

#GET ALL CHARACTERS
@character_routes.route('')
# @login_required
def get_characters():
    characters = Character.query.all()
    return jsonify([char.to_dict() for char in characters])

#GET A SINGLE CHARACTER BY ID
@character_routes.route('/<int:character_id>')
# @login_required
def get_character(character_id):
    character = Character.query.get(character_id)
    if not character:
        return jsonify({"error": "Character not found"}), 404
    return jsonify(character.to_dict())

#CREATE A CHARACTER (LOGIN REQUIRED)
@character_routes.route('', methods=['POST'])
@login_required
def create_character():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    image_url = data.get("image_url")

    if not name or not description or not image_url:
        return jsonify({"error": "All fields are required"}), 400

    new_character = Character(
        name=name,
        description=description,
        image_url=image_url,
        user_id=current_user.id  # Assigns the logged-in user as the creator
    )

    db.session.add(new_character)
    db.session.commit()

    return jsonify(new_character.to_dict()), 201

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
