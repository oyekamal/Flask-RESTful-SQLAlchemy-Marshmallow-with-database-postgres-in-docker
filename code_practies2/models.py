from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'blogposts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    content = db.Column(db.Text, index=True, unique=True)
    date = db.Column(db.DateTime, index=True, unique=True)
    tag = db.Column(db.String(120), index=True, unique=True)
    cover = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
         return '<Post: %r>' % (self.title)