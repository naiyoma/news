
from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()


def create_app(config_name):

    #initializing application
    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)

    #will add the views and forms

    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .request import configure_request
    configure_request(app)

    return app
# 1.i imported the DevConfig class and then used the object method to pass configurations to the DevConfig
# 2.inserting the instance relative config to connect it with the rest of the application