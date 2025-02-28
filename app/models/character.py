from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, DateTime



class Character(db.Model):
    __tablename__ = 'characters'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False) #in production, want to reference correct table
    description = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    created_at = db.Column(DateTime, default=func.now())
    updated_at = db.Column(DateTime, onupdate=func.now())

    #RELATIONSHIP
    user = db.relationship("User", back_populates="characters")
    likes = db.relationship("Like", back_populates="character", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
            'description': self.description,
            'image_url': self.image_url
        }
    def to_dict_with_likes(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
            'description': self.description,
            'image_url': self.image_url,
            'likes': [like.to_dict() for like in self.likes]
        }
