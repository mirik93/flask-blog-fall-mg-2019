from flask import Flask

#Config imports
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#import for flask login
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

#login flow config
login = LoginManager(app)
login.login_veiw = 'login' #this says what page to load

from codingtempleblog import routes,models
