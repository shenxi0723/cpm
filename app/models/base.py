from datetime import datetime

from app.extensions import db
from sqlalchemy import Column, DateTime, SmallInteger

class Base(db.Model):
	__abstract__ = True
	create_time = Column(DateTime, default=datetime.utcnow)
	status = Column(SmallInteger,default=1)
	
	def set_attrs(self,attrs_dict):
		for key,value in attrs_dict.items():
			if hasattr(self,key) and key != 'id':
				setattr(self,key, value)
	
	def __getitem__(self, item):
		return getattr(self,item)
	
	def keys(self):
		return self.fields
	
	#设置不需要返回给客户端的字段
	def hide(self, *field):
		for item in field:
			self.fields.remove(item)
		return self
	
	def delete(self):
		with db.auto_commit():
			self.status = 0