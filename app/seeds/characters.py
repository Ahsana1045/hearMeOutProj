from app.models import db, Character, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo characters, you can add other characters here if you want
def seed_characters():
    optimus = Character(
        name='Optimus',
        user_id=1,
        image_url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/84dc13b7-a2e7-4b45-83ec-311e72e82900/dexyg5k-e12c597d-de9f-4328-812b-14674e05b709.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzg0ZGMxM2I3LWEyZTctNGI0NS04M2VjLTMxMWU3MmU4MjkwMFwvZGV4eWc1ay1lMTJjNTk3ZC1kZTlmLTQzMjgtODEyYi0xNDY3NGUwNWI3MDkucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.rF2e229hKez1OyrZedQiGF6q1cL2VJXlTqbURbCCx5M',
        description='Leader of the Autobots and a Prime. From Transformers')
    goku = Character(
        name='Goku',
        user_id=2,
        image_url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/84dc13b7-a2e7-4b45-83ec-311e72e82900/dexyg5k-e12c597d-de9f-4328-812b-14674e05b709.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzg0ZGMxM2I3LWEyZTctNGI0NS04M2VjLTMxMWU3MmU4MjkwMFwvZGV4eWc1ay1lMTJjNTk3ZC1kZTlmLTQzMjgtODEyYi0xNDY3NGUwNWI3MDkucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.rF2e229hKez1OyrZedQiGF6q1cL2VJXlTqbURbCCx5M',
        description='Saiyan Warrior who chose not to destroy. From DragonBall')
    iceKing = Character(
        name='Ice King',
        user_id=3,
        image_url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/84dc13b7-a2e7-4b45-83ec-311e72e82900/dexyg5k-e12c597d-de9f-4328-812b-14674e05b709.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzg0ZGMxM2I3LWEyZTctNGI0NS04M2VjLTMxMWU3MmU4MjkwMFwvZGV4eWc1ay1lMTJjNTk3ZC1kZTlmLTQzMjgtODEyYi0xNDY3NGUwNWI3MDkucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.rF2e229hKez1OyrZedQiGF6q1cL2VJXlTqbURbCCx5M',
        description='Monarch of the Ice Kingdom. From Adventure Time')

    db.session.add(optimus)
    db.session.add(goku)
    db.session.add(iceKing)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the character table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_characters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.characters RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM characters"))

    db.session.commit()
