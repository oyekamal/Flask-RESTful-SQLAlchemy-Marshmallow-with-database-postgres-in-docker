from .. import db, flask_bcrypt


class Company(db.Model):
    """User Model for storing user related details"""

    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    zip = db.Column(db.String(255), nullable=False)
    registration_number = db.Column(db.String(255), nullable=False)
    registration_court = db.Column(db.String(255), nullable=False)
    vat_number = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "<Company '{}'>".format(self.name)
