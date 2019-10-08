import os
from werkzeug.exceptions import HTTPException
from app.libs.error_code import APIException,ServerError

from app.extensions import cors,db
from app.commands import register_commands
from app.config.setting import config
from app.api import create_blueprint_api_v1
from app.libs.helper import Flask


def create_app(config_name=None):
	if config_name is None:
		config_name = os.getenv('FLASK_CONFIG', 'development')
	
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	
	register_blueprints(app)
	register_extensions(app)
	register_commands(app)
	register_global_errors(app)
	
	return app

def register_blueprints(app):
	bp_v1 = create_blueprint_api_v1()
	app.register_blueprint(bp_v1, url_prefix='/v1')


def register_extensions(app):
	cors.init_app(app, supports_credentials=True)
	db.init_app(app)
	

def register_global_errors(app):
	@app.errorhandler(Exception)
	def global_error(e):
		if isinstance(e, APIException):
			return e
		if isinstance(e, HTTPException):
			code = e.code
			msg = e.description
			error_code = 1007
			return APIException(msg, code, error_code)
		else:
			if not app.config['DEBUG']:
				return ServerError()
			else:
				raise e
	

