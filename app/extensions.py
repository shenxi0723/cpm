from contextlib import contextmanager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery

from app.libs.error_code import NotFound

class Query(BaseQuery):
	def filter_by(self, **kwargs):
		if 'status' not in kwargs.keys():
			kwargs['status'] = 1
		return super(Query,self).filter_by(**kwargs)
	
	def get_or_404(self, ident, description=None):
		rv = self.get(ident)
		if not rv:
			raise NotFound(msg='查询的信息不存在')
		return rv
	
	def first_or_404(self, description=None):
		rv = self.first()
		if not rv:
			raise NotFound(msg='查询的信息不存在')
		return rv


class SQLAlchemy(_SQLAlchemy):
	@contextmanager
	def auto_commit(self):
		try:
			yield
			self.session.commit()
		except Exception as e:
			self.session.rollback()
			raise e


cors = CORS()
db = SQLAlchemy(query_class=Query)