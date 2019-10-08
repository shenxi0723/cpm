from sqlalchemy import Column,Integer,String,SmallInteger,orm,ForeignKey,Boolean
from werkzeug.security import generate_password_hash,check_password_hash

from app.extensions import db
from .base import Base
from app.libs.error_code import NotFound,AuthFailed

class User(Base):
	id = Column(Integer,primary_key=True)
	user_name = Column(String(25),unique=True)
	gender = Column(SmallInteger,default=1)
	email = Column(String(30), unique=True, nullable=False)
	mobile = Column(String(13),nullable=True)
	department_id = Column(Integer,ForeignKey('department.id'),default=None)
	position = Column(String(20),nullable=True)
	auth = Column(SmallInteger,default=1) #权限标识
	is_active = Column(Boolean,default=False)
	__password = Column('password',String(100))
	
	@orm.reconstructor
	def __init__(self):
		self.fields = ['id','email','user_name','auth','is_active','mobile','position','department_id']
	
	@property
	def password(self):
		return self.__password
	
	@password.setter
	def password(self, raw):
		self.__password = generate_password_hash(raw)
	
	@staticmethod
	def register_by_email(user_name,account,secret):
		with db.auto_commit():
			user = User()
			user.user_name = user_name
			user.email = account
			user.password = secret
			db.session.add(user)
	
	@staticmethod
	def create_user(user_name, account, password, gender, department, position, mobile):
		with db.auto_commit():
			user = User()
			user.user_name = user_name
			user.email = account
			user.password = password
			user.department_id = department or None
			user.gender = gender
			user.mobile = mobile
			user.position = position
			db.session.add(user)
			
	@staticmethod
	def edit_user(user_name, account, gender, department, position, mobile):
		user = User.query.filter_by(email = account).first()
		with db.auto_commit():
			user.user_name = user_name
			user.department_id = department or None
			user.gender = gender
			user.mobile = mobile
			user.position = position
			
	
	@staticmethod
	def verify(email, password):
		user = User.query.filter_by(email=email).first()
		if not user:
			raise NotFound(msg='账户不存在！')
		if not user.check_password(password):
			raise AuthFailed(msg='密码错误')
		if not user.check_active():
			raise AuthFailed(msg='该账号没有登录权限')
		return {'uid': user.id, 'auth': user.auth}
	
	def check_password(self,raw):
		if not self.__password:
			return False
		return check_password_hash(self.__password,raw)
	
	def check_active(self):
		return self.is_active
		

from .department import Department