from flask import Flask
from flask_migrate import Migrate
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from resources.item import Item, ItemList, items_ns, item_ns
from marshmallow import ValidationError

from ma import ma 

app = Flask(__name__)
api = Api(app)





app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


db = SQLAlchemy(app)
# ma.init_app(app)

migrate = Migrate(app, db)




api.add_namespace(item_ns)
api.add_namespace(items_ns)


item_ns.add_resource(Item, '/<int:id>')
items_ns.add_resource(ItemList, "")


@app.before_first_request
def create_tables():
    db.create_all()

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True)