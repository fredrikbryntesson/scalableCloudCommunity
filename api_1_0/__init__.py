from flask import Blueprint
from flask_restplus import Api

api1 = Blueprint('api', __name__)
api = Api(api1)

from api_1_0.endpoints.post import nsPost
from api_1_0.endpoints.user import nsUser

api.add_namespace(nsPost)
api.add_namespace(nsUser)