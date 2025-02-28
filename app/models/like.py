from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, DateTime


class Like(db.Model):
    __tablename__ = 'likes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False) #in production, want to reference correct table
    character_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('characters.id')), nullable=False) #in production, want to reference correct table


    #RELATIONSHIPS
    user = db.relationship("User", back_populates="likes") # many-to-many
    character = db.relationship("Character", back_populates="likes")

    def __init__(self, user_id, character_id):
        self.user_id = user_id
        self.character_id = character_id
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }
