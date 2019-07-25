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
    let runModal = function(){
        let BoardId = this.getAttribute("data-board-id");
        showModal(BoardId);
    };
    for (let i = 0; i < newCardButton.length; i++){
        newCardButton[i].addEventListener('click', runModal, false);
    }
    // cancelModal();
}


function renameBoardTitle() {
    let modal = document.getElementById('modal_container');
    let hidden = document.getElementsByClassName('hidden')[0];
    let renameButton = document.getElementsByClassName('rename');
    let board_title = document.getElementById('board_title');
    for (let board of renameButton) {
        board.addEventListener('click', function (event) {
        modal.style.display = 'block';
        board_title.value = event.target.dataset.title;
        hidden.value = 'rename';
        let board_id = event.target.dataset.id;
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
            hiddenInput.value = event.target.dataset.id;
            hiddenInput.value = event.target.dataset.id;
            hidden.value = 'delete';
            deleteModal.style.display = 'block';
        })
    }
    cancelModal(deleteModal, cancelDelete);
}