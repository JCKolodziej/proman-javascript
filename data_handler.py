import persistence, database_common


def get_card_status(status_id):
    """
    Find the first status matching the given id
    :param status_id:
    :return: str
    """
    statuses = persistence.get_statuses()
    return next((status['title'] for status in statuses if status['id'] == str(status_id)), 'Unknown')


def get_boards():
    """
    Gather all boards
    :return:
    """
    return persistence.get_boards(force=True)

@database_common.connection_handler
def get_cards_for_board(cursor, board_id):
    cursor.execute("""
                   SELECT * FROM cards
                   WHERE board_id = %(board_id)s
                   """, {'board_id': board_id})
    cards = cursor.fetchall()
    return cards


@database_common.connection_handler
def get_all_boards(cursor):
    cursor.execute("""
                    SELECT * FROM boards
                    ORDER BY id;
                    """)
    boards = cursor.fetchall()
    return boards


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
