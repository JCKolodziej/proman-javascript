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


def get_cards_for_board(board_id):
    persistence.clear_cache()
    all_cards = persistence.get_cards()
    matching_cards = []
    for card in all_cards:
        if card['board_id'] == str(board_id):
            card['status_id'] = get_card_status(card['status_id'])  # Set textual status for the card
            matching_cards.append(card)
    return matching_cards


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
def delete_board(cursor, board_id):
    cursor.execute("""
                    DELETE FROM boards
                    WHERE id=%(board_id)s;
                    """,
                   {'board_id': board_id})
