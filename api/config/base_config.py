class Config(object):
	DEBUG = False
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'your_secured_key_here'
	SECURITY_PASSWORD_SALT = 'your_security_password_here'

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'your database uri'
	
class DevelopmentConfig(Config):

	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'your database uri'
	SQLALCHEMY_ECHO = False
	MAIL_DEFAULT_SENDER = 'default sender'
	MAIL_SERVER = 'server'
	MAIL_PORT = 'port'
	MAIL_USERNAME = 'username'
	MAIL_PASSWORD = 'password'
	MAIL_USE_TLS = False
	MAIL_USE_SSL = False

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'your database uri'
	SQLALCHEMY_ECHO = False
