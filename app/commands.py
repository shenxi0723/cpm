import click

def register_commands(app):
	@app.cli.command()
	@click.option('--users', default=20, help='Quantity of users, default is 20.')
	def init_db(users):
		from app.extensions import db
		from app.libs.faker import fake_users
		from app.models.user import User
		from app.models.department import Department
		
		db.drop_all()
		db.create_all()
		
		click.echo('Generating %d user account...' % users)
		fake_users()

		click.echo('Finished all.')
		
