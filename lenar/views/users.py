import logging
import json
from flask import Blueprint, jsonify, current_app, request, Response
from storage import STORAGE_CONNECTOR_KEY
from typing import List
from models.user import User
from pydantic import ValidationError

users_view = Blueprint('users_view', __name__)

BASE_URL = "/v1/users"

COLLECTION_NAME = 'users'


@users_view.route(f'{BASE_URL}/ping', methods=['GET'])
def ping():
    logging.info("got ping request")
    return jsonify({'message': "pong"})


@users_view.route(f'{BASE_URL}', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return get_users()
    else:
        try:
            return post_users()
        except ValidationError as e:
            return Response(str(e), 400)


def sanitize_id(documents: List[dict]):
    for d in documents:
        d['_id'] = str(d['_id'])


def get_users():
    logging.info("got users endpoint GET request")
    users_list = current_app.config[STORAGE_CONNECTOR_KEY].find(COLLECTION_NAME)
    sanitize_id(users_list)
    return jsonify({"message": users_list})


def post_users():
    logging.info("got users endpoint POST request")
    user = User(**json.loads(request.data))
    inserted_user = current_app.config[STORAGE_CONNECTOR_KEY].insert_one(COLLECTION_NAME, user.model_dump())
    sanitize_id([inserted_user])
    return jsonify({"message": inserted_user})
