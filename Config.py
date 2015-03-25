import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config():
	SECRET_KEY = os.environ.get("SECRET_KEY") or "hard-to-guess string"

class ProdConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite")

class DevConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or "sqlite:///" + os.path.join(BASE_DIR, "db-development.sqlite")

class TestConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or "sqlite:///" + os.path.join(BASE_DIR, "db-testing.sqlite")

CONFIG = {
	"development": DevConfig,
	"testing": TestConfig,
	"production": ProdConfig
	}