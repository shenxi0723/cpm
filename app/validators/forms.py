from  wtforms import StringField,IntegerField, PasswordField
from wtforms.validators import DataRequired,length,Email,Regexp,ValidationError,NumberRange
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AccountTypeError

from app.validators.base import BaseForm as Form
from app.models.user import User

class ClientForm(Form):
	account = StringField(validators=[DataRequired(message='不允许为空'),length(
		min=5,max=32,message='必须5~32个字符'
	)])
	password = PasswordField()
	type = IntegerField(validators=[DataRequired()])
	
	
	def validate_type(self,value):
		try:
			client = ClientTypeEnum(value.data)
		except ValueError as e:
			raise e
		self.type.data = client


class UserEmailForm(Form):
	account = StringField(validators=[
		Email(message='Invalidate Email')
	])
	secret = PasswordField(validators=[
		DataRequired(),
		Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
	])
	nickname = StringField(validators=[
		DataRequired(),length(min=2, max=22)
	])
	
	def validate_account(self, value):
		if User.query.filter_by(email=value.data).first():
			raise AccountTypeError('该邮箱账户已经存在')

class UserForm(Form):
	account = StringField(validators=[
		DataRequired(message='不允许为空'),
		length(min=5, max=32, message='必须5~32个字符'),
		Email(message='Invalidate Email')
	])
	user_name = StringField(validators=[
		DataRequired(),length(min=2, max=20)
	])
	gender = IntegerField(validators=[
		NumberRange(min=1,max=2)
	])
	department = IntegerField()
	position = StringField()
	mobile = StringField()
	
	def validate_account(self, value):
		if User.query.filter_by(email=value.data).first():
			#raise ValidationError('账户已经存在')
			raise AccountTypeError('该邮箱账户已经存在')

class UserEditForm(UserForm):
	def validate_account(self, value):
		if not User.query.filter_by(email=value.data).first():
			raise AccountTypeError('邮箱账户不存在')