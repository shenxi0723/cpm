from .error import APIException

class ServerError(APIException):
	code = 500
	msg = '服务器错误！'
	error_code = 999

class Success(APIException):
	code = 201
	msg = 'Ok'
	error_code = 0


class AccountTypeError(APIException):
	code = 400
	msg = 'Account is invalid'
	error_code = 1010

class ClientTypeError(APIException):
	code = 400
	msg = 'Client type is invalid.'
	error_code = 1006
	
class ParameterException(APIException):
	code = 400
	msg = 'invalid parameter.'
	error_code = 1000

class NotFound(APIException):
	code = 404
	msg = 'The resource are not found 0.0...'
	error_code = 1001

class AuthFailed(APIException):
	code = 401
	msg = '认证失败'
	error_code = 1005
