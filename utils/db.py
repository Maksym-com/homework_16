import sqlite3

class MyDB:
    def __init__(self, db_file_name) -> None:
        self.db_file_name = db_file_name

    def open(self):
        self.conn = sqlite3.connect(self.db_file_name)
        self.cursor = self.conn.cursor()

    def create_default_table(self):
        """ Creating default table users with fields id, first_name, last_name, username"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL
            );
        """)
        return self.conn.commit()
    
    def user_exists(self, user_id):
        self.cursor.execute("""
            SELECT COUNT(*)
            FROM users
            WHERE id = ?
        """, (user_id, ))
        is_user_exists = self.cursor.fetchone()[0]
        return bool(is_user_exists)

    def add_user_to_db(self, user_id, first_name, last_name, username):
        self.cursor.execute("""
            INSERT INTO users (id, first_name, last_name, username)
            VALUES (?, ?, ?, ?);
        """, (user_id, first_name, last_name, username))
        self.conn.commit()

    def get_my_info(self, username):
        self.cursor.execute("""
            SELECT *
            FROM users
            WHERE username = ?
        """, (username,))
        users = self.cursor.fetchall()
        if users:
            result = ""
            for user_id, first_name, last_name, user_name in users:
                result += f"ID: {user_id}\nUsername: {first_name} @{first_name}\nFirst Name: {last_name}\nLast Name: {user_name}\n\n"
            return result
        else:
            return "Користувача не знайдено"

    def show_all_users(self, user_id, first_name, last_name, username):
        self.cursor.execute("""
            SELECT * FROM users
        """)
        users = self.cursor.fetchall()

        if users:
            result = ""
            for user_id, first_name, last_name, username in users:
                result += f"ID: {user_id}\nFirst Name: {first_name}\nLast Name: {last_name}\nUser Name: {username} @{username}\n\n"
            return result
        else:
            return "Користувачів нема"

    def close(self):
        if hasattr(self, 'conn'):
            self.conn.close()

    
        


