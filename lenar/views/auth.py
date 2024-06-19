import hashlib
import os
from flask import request, jsonify, current_app, Response, Blueprint
from flask_jwt_extended import create_access_token
from bcrypt import hashpw, gensalt, checkpw
from storage import STORAGE_CONNECTOR_KEY
from storage.exceptions import NotFound

auth_view = Blueprint('auth_view', __name__)
BASE_URL = "/v1/users"
COLLECTION_NAME = 'users'


def hash_password(password):
    return hashpw(password.encode('utf-8'), gensalt())


@auth_view.route('/v1/login', methods=['POST'])
def login():
    name = request.json.get("name", None)
    password = request.json.get("password", None)

    if name is None or password is None:
        return Response("request body missing password or username", 400)

    try:
        user_d = current_app.config[STORAGE_CONNECTOR_KEY].find_one(COLLECTION_NAME, {'name': name})
    except NotFound:
        return jsonify({"message": "bad username or password"}), 401

    if not checkpw(password.encode('utf-8'), user_d['password']):
        return jsonify({"msg": "Bad username or password"}), 401

    # Create JWT token
    access_token = create_access_token(identity=str(user_d['_id']))
    return jsonify(access_token=access_token)
