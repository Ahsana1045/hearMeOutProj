from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField
from wtforms.validators import DataRequired, Length, URL

class CharacterForm(FlaskForm):
    name = StringField("Character Name", validators=[
        DataRequired(message="Character name is required"),
        Length(max=50, message="Name cannot exceed 50 characters")
    ])

    description = StringField("Description", validators=[
        DataRequired(message="Description is required"),
        Length(max=100, message="Description cannot exceed 100 characters")
    ])

    image_url = URLField("Image URL", validators=[
        DataRequired(message="Image URL is required"),
        Length(max=5000, message="Image URL cannot exceed 5000 characters"),
        URL(require_tld=True, message="Must be a valid URL")
    ])

    submit = SubmitField("Create Character")
