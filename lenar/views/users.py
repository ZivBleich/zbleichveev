import logging
from flask import Blueprint, jsonify

users = Blueprint('sheet', __name__)

BASE_URL = "v1/users"


@users.route(f'{BASE_URL}/ping', methods=['GET'])
def ping():
    logging.info("got ping request")
    return jsonify({'message': "pong"})
