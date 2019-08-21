import database_common


@database_common.connection_handler
def get_cards_for_board(cursor, board_id):
    cursor.execute("""
                   SELECT * FROM cards
                   WHERE board_id = %(board_id)s
                   """, {'board_id': board_id})
    cards = cursor.fetchall()
    return cards


@database_common.connection_handler
def get_all_public_boards(cursor):
    cursor.execute("""
                    SELECT * FROM boards
                    WHERE user_id  is null 
                    ORDER BY id;
                    """)
    boards = cursor.fetchall()
    return boards


@database_common.connection_handler
def get_private_boards(cursor, user_id):
    cursor.execute('''
                    SELECT * FROM boards
                    WHERE user_id = %(user)s
                    ORDER BY is;
                    ''', {'user': user_id})
    private_boards = cursor.fetchall()
    return private_boards


@database_common.connection_handler
def create_new_board(cursor, board_title):
    cursor.execute("""
                    INSERT INTO boards (title)
                    VALUES (%(board_title)s)
                    """, {'board_title': board_title})


@database_common.connection_handler
def update_board_name(cursor, board_id, board_title):
    cursor.execute("""
                    UPDATE boards
                    SET title = %(board_title)s
                    WHERE id = %(board_id)s;
                    """, {'board_title': board_title,
                          'board_id': board_id})


@database_common.connection_handler
def create_new_card(cursor, card_title, board_id_for_new_card):
    cursor.execute("""
                   INSERT INTO cards (title, board_id, status_id)
                   VALUES (%(card_title)s, %(board_id)s, 0)
                   """, {'card_title': card_title, 'board_id': board_id_for_new_card})


@database_common.connection_handler
def delete_board(cursor, board_id):
    cursor.execute("""
                    DELETE FROM boards
                    WHERE id=%(board_id)s;
                    """,
                   {'board_id': board_id})

@database_common.connection_handler
def get_all_statuses(cursor):
    cursor.execute("""
                   SELECT title FROM statuses;
                   """)
    statues = cursor.fetchall()
    return statues

@database_common.connection_handler
def insert_new_status_title(cursor, new_status_title):
    cursor.execute("""
                   INSERT INTO statuses(title)
                   VALUES (%(title)s)
                   """, {'title': new_status_title})

@database_common.connection_handler
def get_status_id_by_title(cursor, title):
    cursor.execute("""
                   SELECT id FROM statuses WHERE title = %(title)s
                   """, {'title': title})
    status_id = cursor.fetchall()
    return status_id

@database_common.connection_handler
def insert_new_board_status(cursor, board_id, status_id):
    cursor.execute("""
                   INSERT INTO boards_statuses(board_id, status_id)
                   VALUES (%(board_id)s, %(status_id)s)
                   """, {'board_id': board_id, 'status_id': status_id})

@database_common.connection_handler
def get_statuses_for_given_board_id(cursor, board_id):
    cursor.execute("""
                   SELECT statuses.title FROM boards_statuses
                   INNER JOIN boards ON boards_statuses.board_id = boards.id AND boards.id = %(board_id)s
                   INNER JOIN statuses ON boards_statuses.status_id = statuses.id ORDER BY statuses.id
                   """, {'board_id': board_id})
    return cursor.fetchall()
