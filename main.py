import os
import logging

from flask import Flask, jsonify, send_from_directory

from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from api.utils.database import db
from api.utils.responses import response_with
from api.utils.email import mail
import api.utils.responses as resp

from api.routes.authors import author_routes
from api.routes.books import book_routes
from api.routes.users import user_routes

from api.config.config import (
	ProductionConfig,
	TestingConfig,
	DevelopmentConfig
)

app = Flask(__name__)
migrate = Migrate(app, db)

app.config['JWT_SECRET_KEY'] = 'super-secret'

if os.environ.get('FLASK_ENV') == 'PROD':
	app_config = ProductionConfig
elif os.environ.get('FLASK_ENV') == 'DEV':
	app_config = DevelopmentConfig
else:
	app_config = TestingConfig

app.config.from_object(app_config)

app.register_blueprint(author_routes, url_prefix='/api/authors')
app.register_blueprint(book_routes, url_prefix='/api/books')
app.register_blueprint(user_routes, url_prefix='/api/users')

# START GLOBAL HTTP CONF.
@app.after_request
def add_header(response):
	return response

@app.errorhandler(400)
def bad_request(e):
	logging.error(e)
	return resonse_with(resp.BAD_REQUEST_400)

@app.errorhandler(500)
def server_error(e):
	logging.error(e)
	return response_with(resp.SERVER_ERROR_500)

@app.errorhandler(404)
def not_found(e):
	logging.error(e)
	return response_with(resp.SERVER_ERROR_404)

@app.route('/avatar/<filename>', methods=['GET'])
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# to use JWT for authorization
jwt = JWTManager(app)

mail.init_app(app)

db.init_app(app)
with app.app_context():
	db.create_all()

'''
def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)
	
	db.init_app(app)
	with app.app_context():
		db.create_all()
	return app
'''

