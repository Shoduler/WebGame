import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from Config import CONFIG, BASE_DIR

app = Flask(__name__)
app.config.from_object(CONFIG[os.getenv("FLASK_CONFIG") or "development"])

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
lm = LoginManager(app)

from app import Views, Models