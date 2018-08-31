from flask import Flask
from .config import DevConfig
#initializing application
app = Flask(__name__,instance_relative_config=True)

#setting up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views

#we import our child class  and then set it up using the app.config method
# i the connceted my __init__.py with the instance using(app.config.from_pyfile)