from werkzeug.exceptions import HTTPException
from flask import request
import json

class APIException(HTTPException):
	code = 500
	msg = 'Sorry, we make a mistake (*-.-)!'
	error_code = 999
	
	def __init__(self, msg=None, code=None, error_code=None, headers=None):
		if code:
			self.code = code
		if error_code:
			self.error_code = error_code
		if msg:
			self.msg = msg
		super(APIException,self).__init__(msg,None)
	
	def get_body(self, environ=None):
		"""Get the Json Data."""
		body = dict (
			msg = self.msg,
			error_code = self.error_code,
			request = request.method + ' ' +self.get_url_no_params()
		)
		return json.dumps(body)
		
	@staticmethod
	def get_url_no_params():
		full_path = str(request.full_path)
		main_path = full_path.split('?')
		return main_path[0]

	
	def get_headers(self, environ=None):
		"""Get a list of headers."""
		return [("Content-Type", "application/json")]