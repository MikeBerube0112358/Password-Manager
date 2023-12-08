from .database_context_manager import DatabaseConnection
from .password_security import hash_password, verify_password

def create_username_pwd_table() -> None:
    '''Creates SQLite table with auto incrementing user ID, a username and password columns'''
    with DatabaseConnection('hashed_passwords.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        hashed_password_wsalt TEXT NOT NULL);''')

def add_user(username, password):
    '''Adds username and password to SQLite database'''
    with DatabaseConnection('hashed_passwords.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO users (username, hashed_password_wsalt) VALUES(?, ?)', (username, hash_password(password)))
    print("Username and password saved.")

def get_userinfo(id):
    '''Takes a users ID number and returns that users info'''
    with DatabaseConnection('hashed_passwords.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM users WHERE user_id = ?', (id,))
        row = cursor.fetchone()
        if row is not None:
            user = {'id': row[0], 'username': row[1], 'Password': row[2]}
            return user
        else:
            return None

def verify_user(username, password):
    with DatabaseConnection('hashed_passwords.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        if row is not None:
            check_pw = verify_password(row[2], password)
            if check_pw == True:
                print("This is a verified user! \n")
                user = {'id': row[0], 'username': row[1], 'Password': row[2]}
                return user
            else:
                print("Incorrect username or password.\n")
        else:
            print("No user found with this username.\n")
        return None

def get_all_userinfo():
    '''Returns every users info'''
    with DatabaseConnection('hashed_passwords.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM users')
        users = [{'id': row[0], 'username': row[1], 'Password': row[2]} for row in cursor.fetchall()]
    return users

def delete_user(id):
    '''Takes a users id number and deletes that user'''
    with DatabaseConnection('hashed_password.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM users WHERE user_id = ?', (id,))
        #print out the deleted username