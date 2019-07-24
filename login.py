import database_common, bcrypt
from psycopg2 import sql


def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


def register(method, new_login, password):
    if method == 'POST':
        cursor.execute('''
                        SELECT login FROM users
                        ''')
        all_logins = cursor.fetchall()
        if new_login in all_logins:
            return False
        else:
            hashed_password = hash_password(password)
            cursor.execute('''
                            INSERT INTO users (login, password)
                            VALUES (%(new_login)s, %(hashed_password)s)
                            ''',
                           {'new_login': new_login,
                            'hashed_password': hashed_password})
