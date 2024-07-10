from flask import request
from flask_app import app
from flask_app.services.user_service import UserService

http = '/api'


@app.route(http + '/user', methods=['POST'])
def create_user():
    user_id = UserService.create_user(request.json)

    return {
        'id': user_id
    }


@app.route(http + '/users', methods=['GET'])
def read_all_users():
    users = None

    return {
        'users': 'users would go here'
    }