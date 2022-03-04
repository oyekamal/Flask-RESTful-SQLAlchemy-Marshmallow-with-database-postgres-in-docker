from .. import db, flask_bcrypt



class kamal(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "kamal"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
