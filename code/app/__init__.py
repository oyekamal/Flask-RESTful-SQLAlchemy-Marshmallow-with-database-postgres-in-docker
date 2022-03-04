from flask import Blueprint
from flask_restx import Api

from .main.controller.auth_controller import api as auth_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.company_controller import api as company_ns

blueprint = Blueprint("api", __name__)
authorizations = {"apikey": {"type": "apiKey",
                             "in": "header", "name": "Authorization"}}

api = Api(
    blueprint,
    title="Deepgreen Flask Project Backend",
    version="1.0",
    description="a boilerplate for flask restplus (restx) web service",
    authorizations=authorizations,
    security="apikey",
)

api.add_namespace(user_ns, path="/user")
api.add_namespace(auth_ns)
api.add_namespace(company_ns, path="/company")
