from flask import Flask, render_template, url_for, request, session, redirect
from util import json_response
import data_handler
import login

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    """
    This is a one-pager which shows all the boards and cards
    """
    return render_template('index.html')


@app.route("/get-boards")
@json_response
def get_boards():
    """
    All the boards
    """
    return data_handler.get_boards()


@app.route("/get-cards/<int:board_id>")
@json_response
def get_cards_for_board(board_id: int):
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """
    return data_handler.get_cards_for_board(board_id)


@app.route('/test')
def test():
    return render_template('login_test.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return render_template('log.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    return render_template('reg.html')


@app.route('/login_process', methods=['GET', 'POST'])
def login_process():
    if request.method == 'POST':
        username = request.form['usernameLogin']
        password = request.form['passwordLogin']
        if login.login(username, password):
            session['username'] = username
            session['password'] = password
            session['logged_in'] = True
            return render_template('success.html')
        else:
            return render_template('fail.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    session.pop('logged_in', None)
    return redirect(url_for('main'))


@app.route('/registration_process', methods=['GET', 'POST'])
def register_process():
    if request.method == 'POST':
        username = request.form['usernameRegister']
        password = request.form['passwordRegister']
        if login.register(username, password):
            return render_template('success.html')
        else:
            return render_template('fail.html')


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
