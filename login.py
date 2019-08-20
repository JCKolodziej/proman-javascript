import bcrypt
import database_common


def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


@database_common.connection_handler
def register(cursor, new_login, password):
    all_logins = get_logins()
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
        return True


@database_common.connection_handler
def login(cursor, login, password):
    all_logins = get_logins()
    if login in all_logins:
        cursor.execute('''
                        SELECT password FROM users
                        WHERE login = %(login)s
                        ''',
                       {'login': login})
        hashed_password = cursor.fetchall()[0]['password']
        if verify_password(password, hashed_password):
            return True
        else:
            return False


@database_common.connection_handler
def get_logins(cursor):
    cursor.execute('''
                    SELECT login FROM users
                    ''')
    login_list = cursor.fetchall()
    all_users_login = []
    for dict in login_list:
        all_users_login.append(dict['login'])
    return all_users_login
