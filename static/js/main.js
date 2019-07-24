import { dom } from "./dom.js";

// This function is to initialize the application
function init() {
    // init data
    // dom.init();
    // loads the boards to the screen
    // dom.loadBoards();
    addNewBoard();
}

init();

function addNewBoard() {
    let newBoardButton = document.getElementById('top_button');
    newBoardButton.addEventListener('click', showModal);
    cancelModal();
}

function showModal() {
    let modal = document.getElementById('modal_container');
        modal.style.display = 'block';
}

function cancelModal() {
    let modal = document.getElementById('modal_container');
    let cancelButt = document.getElementById('cancel');
    cancelButt.addEventListener('click', function () {
        modal.style.display = 'none';
    })
}