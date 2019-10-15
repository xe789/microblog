from flask import Flask
from config import Config
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin.contrib.sqla import ModelView
from app.models import User

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

admin = Admin(app)
# Add administrative views here
admin.add_view(ModelView(User,db.session))
app.run()

login.login_view = 'login'



