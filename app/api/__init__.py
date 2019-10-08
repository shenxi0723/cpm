from flask import Blueprint
from app.api.v1 import user,asset,client,auth,department


def create_blueprint_api_v1():
	bp_api = Blueprint('api_v1',__name__)
	
	user.api.register(bp_api)
	asset.api.register(bp_api)
	client.api.register(bp_api)
	auth.api.register(bp_api)
	department.api.register(bp_api)
	
	return bp_api
