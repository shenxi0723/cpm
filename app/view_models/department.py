from app.view_models.base import BaseViewModel
from app.extensions import db
from app.models.user import User
from sqlalchemy import func


class DepartmentModel(BaseViewModel):
	def __init__(self,department):
		self.id = department['id']
		self.name = department['name']
		self.count = db.session.query(func.count(User.department_id)).filter(
			User.department_id == department['id']).scalar()
		
	def keys(self):
		return ('id','name','count')


class DepartmentCollection(BaseViewModel):
	def __init__(self):
		self.total = 0
		self.department = []
		
	def get_department(self, department_list):
		self.total = len(department_list) or 0
		self.department = [ DepartmentModel(department) for department in department_list ]
		
	def keys(self):
		return ('total','department')
	

