from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired, length,NumberRange
from app.libs.error_code import AccountTypeError

from app.validators.base import BaseForm as Form
from app.models.department import Department


class DepartmentForm(Form):
	name = StringField(validators=[
		DataRequired(message='不允许为空'),
		length(min=1, max=20, message='必须1~20个字符'),
	])

	def validate_name(self, value):
		if Department.query.filter_by(name=value.data).first():
			raise AccountTypeError('该部门已经存在')

class DepartmentEditForm(DepartmentForm):
	id = IntegerField(validators=[DataRequired(message='没有提供id')])

class DepartmentDeleteForm(DepartmentEditForm):
	count = IntegerField(validators=[NumberRange(min=0)])
	
	def validate_name(self, value):
		if not Department.query.filter_by(name=value.data).first():
			raise AccountTypeError('删除的部门不存在')
		
	def validate_count(self,value):
		if value.data > 0:
			raise AccountTypeError('该部门下还有成员')