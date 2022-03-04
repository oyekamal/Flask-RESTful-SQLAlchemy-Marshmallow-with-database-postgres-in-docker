from flask_restx import Namespace, fields


class UserDto:
    api = Namespace("user", description="user related operations")
    user = api.model(
        "user",
        {
            "email": fields.String(required=True, description="user email address"),
            "username": fields.String(required=True, description="user username"),
            "password": fields.String(required=True, description="user password"),
            "public_id": fields.String(description="user Identifier"),
        },
    )


class AuthDto:
    api = Namespace("auth", description="authentication related operations")
    user_auth = api.model(
        "auth_details",
        {
            "email": fields.String(required=True, description="The email address"),
            "password": fields.String(required=True, description="The user password "),
        },
    )


class CompanyDto:
    api = Namespace("Company", description="Company for user/customer")
    campany = api.model(
        "companies",
        {
            "name": fields.String(required=True, description="The name of company"),
            "address": fields.String(required=True, description="The address "),
            "city": fields.String(required=True, description="The city "),
            "state": fields.String(required=True, description="The state "),
            "zip": fields.String(required=True, description="The zip "),
            "registration_number": fields.String(required=True, description="The registration_number "),
            "registration_court": fields.String(required=True, description="The registration_court "),
            "vat_number": fields.String(required=True, description="The vat_number ")
        },
    )
