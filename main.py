from flask import Flask, render_template, url_for, request, session, redirect

import data_handler
import login
import json


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        card_request = request.form.get('board_id_for_new_card')
        if card_request:
            card_title = request.form['card_title']
            board_id_for_new_card = request.form['board_id_for_new_card']
            data_handler.create_new_card(card_title, board_id_for_new_card)
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
        return redirect('/')
    else:
        boards = data_handler.get_all_boards()
        cards = []
        for board in boards:
            cards.append(data_handler.get_cards_for_board(board['id']))
        return render_template('index.html', boards=boards, cards=cards)


def delete_board(board_id):
    data_handler.delete_board(board_id)


@app.route('/login_process', methods=['GET', 'POST'])
def login_process():
    if request.method == 'POST':
        user = json.loads(request.data)
        username = user['login']
        password = user['password']
        if login.login(username, password):
            session['username'] = username
            session['logged_in'] = True
            return json.dumps({'success': True})
        else:
            session['error_login'] = True
            return json.dumps({'success': False})


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('index'))


@app.route('/registration_process', methods=['GET', 'POST'])
def register_process():
    if request.method == 'POST':

        session['error_login'] = False
        username = request.form['usernameRegister']
        password = request.form['passwordRegister']
        if login.register(username, password):
            login.login(username, password)
            session['username'] = username
            session['password'] = password
            session['logged_in'] = True
            session['error_register'] = False
            return redirect(url_for('index'))
        else:
            session['error_register'] = True
            return redirect(url_for('index'))


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
