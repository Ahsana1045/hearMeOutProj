from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import db, Like, Character

like_routes = Blueprint("likes", __name__)

# GET: Get the number of likes on a character
@like_routes.route('/<int:character_id>/likes', methods=['GET'])
def get_likes(character_id):
    likes = Like.query.filter_by(character_id=character_id).all()
    return jsonify({
        "character_id": character_id,
        "likes_count": len(likes),
        "users": [like.to_dict() for like in likes]
    }), 200

# POST: User likes a character
@like_routes.route('/<int:character_id>/likes', methods=['POST'])
@login_required
def like_character(character_id):
    # Check if the character exists
    character = Character.query.get(character_id)
    if not character:
        return jsonify({"error_message": "Character not found"}), 404

    # Check if user already liked this character
    like_exists = Like.query.filter_by(user_id=current_user.id, character_id=character_id).first()
    if like_exists:
        return jsonify({"error_message": "User has already liked this character"}), 400

    # Create a new like
    new_like = Like(user_id=current_user.id, character_id=character_id)
    db.session.add(new_like)
    db.session.commit()

    return jsonify({
        "message": "User successfully liked this character!",
        "new_like_id": new_like.id,
        "character_id": character_id,
        "user_id": current_user.id
    }), 201

# DELETE: User unlikes a character
@like_routes.route('/<int:character_id>/likes', methods=['DELETE'])
@login_required
def unlike_character(character_id):
    like = Like.query.filter_by(user_id=current_user.id, character_id=character_id).first()

    if not like:
        return jsonify({"error_message": "Like not found"}), 404

    db.session.delete(like)
    db.session.commit()

    return jsonify({
        "message": "User successfully unliked this character",
        "character_id": character_id
    }), 200
