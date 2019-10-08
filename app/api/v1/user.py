from flask import jsonify
from sqlalchemy import desc

from flask import current_app
from app.libs.redprint import Redprint
from app.libs.toke_auth import auth
from app.models.user import User
from app.view_models.users import UserCollection
from app.libs.error_code import Success
from app.validators.forms import UserForm, UserEditForm

api = Redprint('user')

@api.route('/<int:uid>',methods=['GET'])
@auth.login_required
def get_user(uid):
	user = User.query.get_or_404(uid)
	return jsonify(user)


@api.route('',methods=['GET'])
@auth.login_required
def get_users():
	users = User.query.order_by(desc(User.create_time)).all()
	users = [user.hide('id','auth','is_active') for user in users]
	
	#使用ViewModel
	users_view = UserCollection()
	users_view.get_member(users)
	
	return jsonify(users_view)


@api.route('', methods=['POST'])
@auth.login_required
def add_user():
	form = UserForm().validate_for_api()
	default_user_password = current_app.config['USER_INIT_PASSWORD']
	User.create_user(
		form.user_name.data, form.account.data, default_user_password,
		form.gender.data, form.department.data, form.position.data, form.mobile.data)
	return Success(msg='用户添加成功')


@api.route('', methods=['PUT'])
@auth.login_required
def edit_user():
	form = UserEditForm().validate_for_api()
	User.edit_user(form.user_name.data, form.account.data,
		form.gender.data, form.department.data, form.position.data, form.mobile.data)
	return Success(msg='用户信息修改成功')