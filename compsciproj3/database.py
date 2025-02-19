import sqlite3
class DatabaseManager:
    def __init__(self, name: str):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()
    def execute(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def close(self):
        self.connection.close()

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

