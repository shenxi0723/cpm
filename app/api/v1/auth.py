from itsdangerous import TimedJSONWebSignatureSerializer as Serial
from flask import current_app,jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from app.models.user import User

api = Redprint('auth')

@api.route('', methods=['POST'])
def get_token():
	form = ClientForm().validate_for_api()
	#区分不同的客户端
	promise = {
		ClientTypeEnum.USER_EMAIL: User.verify,
	}
	identity = promise[ClientTypeEnum(form.type.data)](
		form.account.data,
		form.password.data
	)
	# 生成令牌Token
	expiration = int(current_app.config['TOKEN_EXPIRATION'])
	token = generate_auth_token(
		identity['uid'], identity['auth'] ,form.type.data, None, expiration)
	t = {
		'token': token.decode('ascii'),
		'auth': identity['auth']
	}
	return jsonify(t), 201

def generate_auth_token(uid,auth,ac_type,scope=None,expiration=7200):
	s = Serial(current_app.config['SECRET_KEY'], expires_in=expiration)
	return s.dumps({
		'uid': uid,
		'auth': auth,
		'type': ac_type.value
	})