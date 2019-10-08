from flask import g
from app.view_models.base import BaseViewModel

class UserViewModel(BaseViewModel):
	def __init__(self, user):
		self.user_id = user['id']
		self.user_name = user['user_name']
		self.gender = str(user['gender'])
		self.email = user['email']
		self.mobile = user['mobile'] or '无'
		self.department = user['department_id']
		self.position = user['position'] or '无'
	
	def keys(self):
		return ('user_name','gender','email','mobile','department','position')


class UserCollection(BaseViewModel):
	def __init__(self):
		self.total = 0
		self.users = []
		self.user_auth = 1
		
	def get_member(self,users):
		self.total = len(users) or 0
		self.users = [UserViewModel(user) for user in users]
		self.user_auth = g.user.auth
		
		# 也可以不对单个条目进行修饰
		# self.users = users
		
	def keys(self):
		return ('total', 'users', 'user_auth')
	