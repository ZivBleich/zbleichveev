import logging
import json
from flask import Blueprint, jsonify, current_app, request, Response
from storage import STORAGE_CONNECTOR_KEY
from storage.exceptions import NotFound
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
        return _get_users()
    else:
        try:
            return _post_users()
        except ValidationError as e:
            return Response(str(e), 400)


def _get_users():
    logging.info("got users endpoint GET request")
    users_list = current_app.config[STORAGE_CONNECTOR_KEY].find(COLLECTION_NAME)
    return jsonify({"message": users_list})


def _post_users():
    logging.info("got users endpoint POST request")
    user = User(**json.loads(request.data))
    inserted_user = current_app.config[STORAGE_CONNECTOR_KEY].insert_one(COLLECTION_NAME, user.model_dump())
    return jsonify({"message": inserted_user})


@users_view.route(f'{BASE_URL}/<user_id>', methods=['PATCH'])
def update_user(user_id: str):
    logging.info("got users endpoint PATCH request")

    try:
        return _update_user(user_id)
    except ValidationError as e:
        return Response(str(e), 400)
    except NotFound as e:
        return Response(str(e), 404)


def _update_user(user_id: str):
    user = User(**json.loads(request.data))
    updated_user = current_app.config[STORAGE_CONNECTOR_KEY].update_one(COLLECTION_NAME, user_id, user.model_dump())
    return jsonify({"message": updated_user})


@users_view.route(f'{BASE_URL}/<user_id>', methods=['DELETE'])
def delete_user(user_id: str):
    logging.info("got users endpoint DELETE request")
    try:
        return _delete_user(user_id)
    except ValidationError as e:
        return Response(str(e), 400)
    except NotFound as e:
        return Response(str(e), 404)


def _delete_user(user_id: str):
    current_app.config[STORAGE_CONNECTOR_KEY].delete_one(COLLECTION_NAME, user_id)
    return jsonify({"message": "SUCCESS"})
