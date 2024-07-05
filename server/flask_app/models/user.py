from flask_app.config.postgresconnection import connectToPostgres

class User:
    DB = 'postgres'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']

    @classmethod
    def create_user(cls, data):
        query = """
                INSERT INTO users (name)
                values(%(name)s)
                """
        return connectToPostgres().query_db(query, data)