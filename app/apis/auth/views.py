from flask import Blueprint, request

from app.extensions import oauth
from app.utilities.schema_validators import validate_request_schema
from app.utilities.api_result import ApiResult

from .schemas import LoginSchema
from .services.user_auth_service import UserAuthService

auth = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth.route('/oauth/token', methods=['POST'])
@oauth.token_handler
def access_token():
    """To Create Oauth Tokens"""
    return None


@auth.route('/login', methods=['POST'])
@validate_request_schema(schema=LoginSchema)
def login():
    """Log a user in using oauth/token"""
    # Use Oauth library to validate and give a token to the user
    data = request.json
    return UserAuthService().login_user(data['username'], data['password'])