"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# Logging: send INFO-and-above messages (including login attempts) to a
# stream handler. On Azure App Service this shows up in the Log stream
# under Monitoring > App Service logs, once application logging is turned on.
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s in %(module)s: %(message)s'
))
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
