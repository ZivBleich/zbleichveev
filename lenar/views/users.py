import logging
from flask import Blueprint, jsonify, current_app
from models.ping import Ping

users = Blueprint('sheet', __name__)

BASE_URL = "/v1/users"


@users.route(f'{BASE_URL}/ping', methods=['GET'])
def ping():
    logging.info("got ping request")
    db = current_app.config['mongo_client']['lenar']
    db['ping'].insert_one(Ping(hello="world").model_dump())
    logging.info([item for item in db['ping'].find({})])
    return jsonify({'message': "pong"})
