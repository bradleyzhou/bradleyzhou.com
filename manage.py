import os

from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from app import db
from app import create_app
from app.models import Role
from app.models import User
from app.models import Post

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
app.cli.add_command(MigrateCommand, name='db')


@app.cli.command()
def fake():
    """Generate some fake data"""
    Role.insert_roles()
    u1 = User(username='me',
              email='a@b.com',
              password='cat',
              )
    u2 = User(username='he',
              email='b@b.com',
              password='dog',
              )
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()
    Post.generate_fake(15)
