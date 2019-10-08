import os

class BaseConfig:
	SECRET_KEY = os.getenv('SECRET_KEY', 'secret#￥%Key')
	USER_INIT_PASSWORD = os.getenv('USER_INIT_PASSWORD', '123456')
	TOKEN_EXPIRATION = os.getenv('TOKEN_EXPIRATION', 3600)
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
class DevelopmentConfig(BaseConfig):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + os.getenv('DATABASE_URI')

class TestingConfig(BaseConfig):
	TESTING = True
	WTF_CSRF_ENABLED = False

class ProductionConfig(BaseConfig):
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + os.getenv('DATABASE_URI')

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig
}