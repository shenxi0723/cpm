from  wtforms import Form
from flask import request

from app.libs.error_code import ParameterException


class BaseForm(Form):
	def __init__(self):
		data = request.get_json(silent=True)
		super(BaseForm,self).__init__(data=data)
	
	
	def validate_for_api(self):
		valid = super(BaseForm,self).validate()
		if not valid:
			raise ParameterException(msg=self.errors)
		return self