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
}

init();

function addNewBoard() {
    let newBoardButton = document.getElementById('addNewBoardBtn');
    newBoardButton.addEventListener('click', showModal);
    cancelModal();
}

function showModal(BoardId) {
    let hidden = document.getElementById('hidden');
    let modal = document.getElementById('modal_container');
        modal.style.display = 'block';
    document.getElementById('board_id').value = BoardId;
        hidden.value = 'new';
}

function cancelModal() {
    let modal = document.getElementById('modal_container');
    let cancelButt = document.getElementById('cancel');
    cancelButt.addEventListener('click', function () {
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
    cancelModal();
}


function renameBoardTitle() {
    let modal = document.getElementById('modal_container');
    let hidden = document.getElementById('hidden');
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
