from  flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serial, BadSignature,SignatureExpired
from flask import current_app,g
from collections import namedtuple

from app.libs.error_code import AuthFailed

auth = HTTPTokenAuth(scheme='Bearer')
User = namedtuple('User',['uid','ac_type','auth','scope'])

@auth.verify_token
def verify_token(token):
	user_info = verify_auth_token(token)
	if not user_info:
		return False
	else:
		g.user = user_info
		return True
	
def verify_auth_token(token):
	s = Serial(current_app.config['SECRET_KEY'])
	try:
		data = s.loads(token)
	except BadSignature:
		raise  AuthFailed(msg='非法身份，请重新登录',error_code=1002)
	except SignatureExpired:
		raise AuthFailed(msg='身份过期，请重新登录',error_code=1003)
	
	uid= data['uid']
	ac_type = data['type']
	auth= data['auth']
	return User(uid,ac_type,auth,'')
