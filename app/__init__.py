from flask import Flask
from app.config import DevConfig
from flask_bootstrap import Bootstrap

#Initializing the app
app = Flask(__name__, instance_relative_config = True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing flask extensions
bootstrap = Bootstrap(app)

from app import views