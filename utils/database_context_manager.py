import sqlite3

class DatabaseConnection:
    def __init__(self, db_file) -> None:
        self.connection = None
        self.host = db_file

    def __enter__(self):
        self.connection = sqlite3.connect('hashed_passwords.db')
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()