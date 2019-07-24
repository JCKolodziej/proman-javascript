import { dom } from "./dom.js";

// This function is to initialize the application
function init() {
    // init data
    // dom.init();
    // loads the boards to the screen
    // dom.loadBoards();
    addNewBoard();
    addNewCard();
}

init();

function addNewBoard() {
    let newBoardButton = document.getElementById('addNewBoardBtn');
    newBoardButton.addEventListener('click', showModal);
    cancelModal();
}

function showModal(BoardId) {
    let modal = document.getElementById('modal_container');
        modal.style.display = 'block';
    document.getElementById('board_id').value = BoardId;
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

/*
*
var classname = document.getElementsByClassName("classname");

var myFunction = function() {
    var attribute = this.getAttribute("data-myattribute");
    alert(attribute);
};

for (var i = 0; i < classname.length; i++) {
    classname[i].addEventListener('click', myFunction, false);
}
* */