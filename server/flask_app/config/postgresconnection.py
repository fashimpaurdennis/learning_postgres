import psycopg2 as p

class PostgresConnection:
    def __init__(self):
        self.connection = p.connect("dbname=test user=postgres password=root host=localhost port=5432")
        self.connection.autocommit = True

    def query_db(self, query, data=None):
        with self.connection.cursor() as cur:
            try:
                print("Running Query: ", query)
                cur.execute(query, data)
                if query.strip().lower().find('insert') >= 0:
                    self.connection.commit()
                    return str(cur.lastrowid)
                elif query.lower().find('select') >= 0:
                    result = cur.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong: ", e)
                return False
            finally:
                self.connection.close()


def connectToPostgres():
    return PostgresConnection()
