from flask_app.models.user import User
from flask_app.config.postgresconnection import connectToPostgres


class UserService:

    def __init__(self, user):
        self.user = user

    @classmethod
    def create_user(cls, data):
        query = """
                INSERT INTO users (name)
                values(%(name)s)
                """
        return connectToPostgres().query_db(query, data)
