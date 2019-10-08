from faker import Faker
from app.models.user import User

fake = Faker('zh_CN')

def fake_users(count=20):
	for i in range(count):
		User.register_by_email(
			fake.name(),
			fake.email(),
			'123456'
			#fake.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
		)