import os
import unittest

from flask_migrate import Migrate

from app import blueprint
from app.main import create_app, db
from app.main.model import blacklist, company, user

# from flask_script import Manager


app = create_app("dev")
app.register_blueprint(blueprint)

app.app_context().push()


migrate = Migrate(app, db)


def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    app.run()
