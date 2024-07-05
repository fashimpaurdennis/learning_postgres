from flask_app import app
from flask_app.models.user import User

@app.route('/api/user', methods=['POST'])
def create_user():

    user_id = User.create_user(request.json)

    return {
        'id': user_id
    }
