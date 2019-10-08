from flask import jsonify
from app.libs.redprint import Redprint

from app.libs.toke_auth import auth
from app.models.department import Department
from app.view_models.department import DepartmentCollection
from app.validators.department import DepartmentForm,DepartmentEditForm,DepartmentDeleteForm
from app.libs.error_code import Success


api = Redprint('department')


@api.route('/<int:id>', methods=['GET'])
@auth.login_required
def get_department(id):
	department = Department.query.get_or_404(id)
	return jsonify(department)


@api.route('', methods=['GET'])
@auth.login_required
def get_department_schema():
	department = Department.query.all()
	
	# 使用ViewModel
	department_view = DepartmentCollection()
	department_view.get_department(department)
	return jsonify(department_view)


@api.route('', methods=['POST'])
@auth.login_required
def add_department():
	form = DepartmentForm().validate_for_api()
	Department.create(form.name.data)
	return Success(msg='部门添加成功')


@api.route('',methods=['PUT'])
@auth.login_required
def edit_department():
	form = DepartmentEditForm().validate_for_api()
	Department.edit(form.id.data, form.name.data)
	return Success(msg='部门修改成功')


@api.route('',methods=['DELETE'])
@auth.login_required
def remove_department():
	form = DepartmentDeleteForm().validate_for_api()
	Department.delete(form.id.data)
	
	return Success(msg='部门删除成功')

