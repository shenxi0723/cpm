from sqlalchemy import Column,Integer,String,orm

from app.extensions import db
from .base import Base
from app.libs.error_code import NotFound,AuthFailed

class Department(Base):
	__tablename__ = 'department'
	id = Column(Integer,primary_key=True)
	name= Column(String(30),unique=True,nullable=False)
	user = db.relationship("User",backref='department', lazy='dynamic')
	
	@orm.reconstructor
	def __init__(self):
		self.fields = ['id', 'name']
		
		
	@staticmethod
	def create(name):
		with db.auto_commit():
			department = Department()
			department.name = name
			db.session.add(department)
	
	@staticmethod
	def edit(id,new_name):
		department = Department.query.get_or_404(id)
		with db.auto_commit():
			department.name = new_name
	

	@staticmethod
	def delete(id):
		department = Department.query.get_or_404(id)
		with db.auto_commit():
			db.session.delete(department)
	
	def __str__(self):
		return self.name
		
	