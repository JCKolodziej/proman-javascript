import json

from flask import Flask, render_template, url_for, request, session, redirect

import data_handler
import login

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        card_request = request.form.get('board_id_for_new_card')
        if card_request:
            card_title = request.form['card_title']
            board_id_for_new_card = request.form['board_id_for_new_card']
            new_card_status = data_handler.get_statuses_for_given_board_id(board_id_for_new_card)
            data_handler.create_new_card(card_title, board_id_for_new_card, new_card_status[0]['id'])
            return redirect('/')

        column_request = request.form.get('board_id_for_new_column')
        if column_request:
            new_column_title = request.form['column_title']
            board_id_for_new_column = request.form['board_id_for_new_column']
            # checking for existing statues title
            all_statuses = data_handler.get_all_statuses()
            if new_column_title not in all_statuses:
                data_handler.insert_new_status_title(new_column_title)

            new_status_id = data_handler.get_status_id_by_title(new_column_title)
            data_handler.insert_new_board_status(board_id_for_new_column, new_status_id[0]['id'])
            return redirect('/')

        rename_column_title_request = request.form.get('status_id_for_new_column_title')
        if rename_column_title_request:
            renamed_column_title = request.form['new_column_title']
            status_id_for_new_title = request.form['status_id_for_new_column_title']
            data_handler.rename_status_title(status_id_for_new_title, renamed_column_title)
            return redirect('/')

        action_type = request.form['hidden']
        if action_type == 'delete':
            delete_id = request.form['delete_id']
            data_handler.delete_board(delete_id)
            return redirect('/')

        board_title = request.form['board_title']
        if action_type == 'rename':
            board_id = request.form['board_id']
            data_handler.update_board_name(board_id, board_title)
            return redirect('/')
        elif action_type == 'new':
            data_handler.create_new_board(board_title)
            return redirect('/')

        private_type = request.form['privateHidden']
        if private_type == 'private':
            user_id = session['user_id']
            private_title = request.form['private_title']
            data_handler.create_new_private_board(private_title, user_id)
        return redirect('/')
    else:
        boards = data_handler.get_all_public_boards()
        private_boards = {}
        cards = []
        private_cards = []
        statuses = []
        private_statuses = []
        if session:
            user_id = session['user_id']
            private_boards = data_handler.get_private_boards(user_id)
            for private in private_boards:
                private_cards.append(data_handler.get_cards_for_board(private['id']))
                private_statuses.append(data_handler.get_statuses_for_given_board_id(private['id']))
        for board in boards:
            cards.append(data_handler.get_cards_for_board(board['id']))
            statuses.append(data_handler.get_statuses_for_given_board_id(board['id']))
        return render_template('index.html', boards=boards, cards=cards, statuses=statuses, private_cards=private_cards,
                               private_boards=private_boards, private_statuses=private_statuses)


def delete_board(board_id):
    data_handler.delete_board(board_id)


@app.route('/login_process', methods=['GET', 'POST'])
def login_process():
    if request.method == 'POST':
        user = json.loads(request.data)
        username = user['login']
        password = user['password']
        user_id = login.login(username, password)
        if user_id:
            session['username'] = username
            session['user_id'] = user_id
            session['logged_in'] = True
            return json.dumps({'success': True})
        else:
            return json.dumps({'success': False})


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('logged_in', None)
    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/register_process', methods=['GET', 'POST'])
def register_process():
    if request.method == 'POST':
        user = json.loads(request.data)

        username = user['login']
        password = user['password']
        user_id = login.register(username, password)
        if user_id:
            login.login(username, password)
            session['username'] = username
            session['logged_in'] = True
            session['user_id'] = user_id
            return json.dumps({'success': True})
        else:
            return json.dumps({'success': 'in_use'})


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
