import atexit
from logging.config import dictConfig
from flask import Flask
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
from .views.users import users_view
from .views.auth import auth_view
from .storage import STORAGE_CONNECTOR_KEY
from .storage.mongo_storage_connector import MongoStorageConnector

DB_NAME = 'lenar'
MONGO_SERVER = 'localhost'
MONGO_PORT = 27017

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

# jwt
app.config['JWT_SECRET_KEY'] = 'verysecret'
jwt = JWTManager(app)

# mongodb
app.config[STORAGE_CONNECTOR_KEY] = MongoStorageConnector(MongoClient(MONGO_SERVER, MONGO_PORT), DB_NAME)


def close_connection():
    app.config[STORAGE_CONNECTOR_KEY].close()


atexit.register(close_connection)
app.register_blueprint(users_view)
app.register_blueprint(auth_view)
