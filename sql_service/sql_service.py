class SQLService:
    def __init__(self, connection):
        self.connection = connection

    def execute_select_query(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data
