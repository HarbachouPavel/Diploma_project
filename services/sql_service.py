class SQLService:
    def __init__(self, connection):
        self.connection = connection

    def sql_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data
