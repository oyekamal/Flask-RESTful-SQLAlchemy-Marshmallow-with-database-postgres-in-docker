import datetime
from flask import Flask, render_template
from flask_migrate import Migrate
# from flask_s3 import FlaskS3
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)
migrate = Migrate(app, db)
# s3 = FlaskS3(app)
from models import Post


@app.route('/add/')
def webhook():
    #post attributes defined
    p = Post(id = 1, title = "title", date = datetime.datetime.utcnow, content = "content", tag = "tag", cover = "cover")
    print("post created", p)
    db.session.add(p)
    db.session.commit()
    return "post created"
#routes to templates to be rendered

if __name__ == '__main__':
    app.run(debug=True)