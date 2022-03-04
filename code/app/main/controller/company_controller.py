from typing import Dict, Tuple

from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import CompanyDto


api = CompanyDto.api
_company = CompanyDto.campany


@api.route("/")
class Company(Resource):
    # @api.doc("get a user")
    # @api.marshal_with(_company)
    def get(self):
        return {"company": "kamal"}
