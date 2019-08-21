import { dom } from "./dom.js";

// This function is to initialize the application
function init() {
    // init data
    // dom.init();
    // loads the boards to the screen
    // dom.loadBoards();
    addNewBoard();
    addNewCard();
    renameBoardTitle();
    deleteBoard();
    loadDragula();
    loginProcess();
    addNewColumn();
}

init();

function addNewBoard() {
    let newBoardButton = document.getElementById('addNewBoardBtn');
    let modal = document.getElementById('modal_container');
    newBoardButton.addEventListener('click', showModal);
    let cancelButt = document.getElementById('cancel');
    cancelModal(modal, cancelButt);
}

function showModal() {
    let hidden = document.getElementsByClassName('hidden')[0];
    let modal = document.getElementById('modal_container');
        modal.style.display = 'block';
        hidden.value = 'new';
}

function cancelModal(modal, button) {
    button.addEventListener('click', function () {
        modal.style.display = 'none';
    })
}

function addNewCard() {
    let newCardButton = document.getElementsByClassName('addNewCardBtn');
    let CardModal = document.getElementById('modal_for_add_card');
    let runModalForNewCard = function(){
        let BoardId = this.getAttribute("data-board-id");
        CardModal.style.display = 'block';
        document.getElementById('board_id_for_new_card').setAttribute('value', BoardId);
    };
    for (let i = 0; i < newCardButton.length; i++){
        newCardButton[i].addEventListener('click', runModalForNewCard, false);
    }
    cancelModal(CardModal, document.getElementById('cancel_for_card_modal'));
}

function addNewColumn() {
    let newColumnButton = document.getElementsByClassName('addNewColumnBtn');
    let ColumnModal = document.getElementById('modal_for_add_column');
    let runModalForNewColumn = function(){
        let BoardIdForNewColumn = this.getAttribute("data-board-id");
        console.log(BoardIdForNewColumn);
        ColumnModal.style.display = 'block';
        document.getElementById('board_id_for_new_column').setAttribute('value', BoardIdForNewColumn);
    };
    for (let i = 0; i < newColumnButton.length; i++){
        newColumnButton[i].addEventListener('click', runModalForNewColumn , false);
    }
    cancelModal(ColumnModal, document.getElementById('cancel_for_column_modal'));
}

function renameBoardTitle() {
    let modal = document.getElementById('modal_container');
    let hidden = document.getElementsByClassName('hidden')[0];
    let renameButton = document.getElementsByClassName('rename');
    let board_title = document.getElementById('board_title');
    for (let board of renameButton) {
        board.addEventListener('click', function (event) {
            modal.style.display = 'block';
            board_title.value = board.dataset.title;
            hidden.value = 'rename';
            let board_id = board.dataset.id;
            createHiddenInput(board_id);
        })
    }
}

function createHiddenInput(value) {
    let input = document.createElement('input');
    let form = document.getElementById('board_form');
    input.type = 'hidden';
    input.value = value;
    input.name = 'board_id';
    input.id = 'board_id';
    form.appendChild(input);
}

function deleteBoard() {
    let deleteButtons = document.getElementsByClassName('delete');
    let deleteModal = document.getElementById('delete_modal');
    let hiddenInput = document.getElementById('delete_id');
    let cancelDelete = document.getElementById('cancel_delete');
    let hidden = document.getElementsByClassName('hidden')[1];
    for (let deleteButton of deleteButtons) {
        deleteButton.addEventListener('click', function (event) {
            hiddenInput.value = deleteButton.dataset.id;
            hiddenInput.value = deleteButton.dataset.id;
            hidden.value = 'delete';
            deleteModal.style.display = 'block';
        })
    }
    cancelModal(deleteModal, cancelDelete);
}


function loadDragula() {
    $('document').ready(function () {
        let drake = dragula({
            isContainer: function (el) {
                return el.classList.contains('dragula-container');
            }
        });
    });

}

export function loginProcess() {
    let loginForm = document.getElementById('loginForm');
    let submitButton = document.getElementById('loginButton');
    submitButton.addEventListener("submit", function (event) {
        event.preventDefault();
        loginForm.addEventListener("submit", function (event) {
            event.preventDefault()
        })
    });

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();
        let username = document.getElementById('defaultForm-username');
        let password = document.getElementById('defaultForm-pass');
        validationChecker(username.value, password.value)
    })
}


function validationChecker(login, password) {
    let validationData = {
        login: login,
        password: password
    };
    console.log(validationData);
    fetch('/login_process', {
        method: 'POST',
        mode: "same-origin",
        credentials: "same-origin",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(validationData)

    })
        .then(response => response.json())
        .then(validation => {
            if (validation.success === true) {
                window.location.replace('/');
                console.log(validation);
            } else {
                let alertBar = document.getElementById('invalidCredentials');
                console.log(validation);
                alertBar.style.display = 'block'
            }
        })
}