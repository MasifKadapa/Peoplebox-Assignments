const board = document.getElementById('board');
const cells = document.querySelectorAll('.cell');
const message = document.getElementById('message');
const resetButton = document.getElementById('reset');
const currentPlayerDisplay = document.getElementById('player');
const scoreXDisplay = document.getElementById('scoreX');
const scoreODisplay = document.getElementById('scoreO');
const clickSound = document.getElementById('clickSound');
const winSound = document.getElementById('winSound');

let currentPlayer = 'X';
let gameActive = true;
let gameState = ['', '', '', '', '', '', '', '', ''];
let scoreX = 0;
let scoreO = 0;

const winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

function handleCellClick(event) {
    const clickedCell = event.target;
    const clickedCellIndex = parseInt(clickedCell.getAttribute('data-index'));

    if (gameState[clickedCellIndex] !== '' || !gameActive) {
        return;
    }

    gameState[clickedCellIndex] = currentPlayer;
    clickedCell.textContent = currentPlayer;
    clickSound.play();

    checkResult();
}

function checkResult() {
    let roundWon = false;

    for (let i = 0; i < winningConditions.length; i++) {
        const [a, b, c] = winningConditions[i];
        if (gameState[a] === '' || gameState[b] === '' || gameState[c] === '') {
            continue;
        }
        if (gameState[a] === gameState[b] && gameState[a] === gameState[c]) {
            roundWon = true;
            highlightWinningCells(a, b, c);
            break;
        }
    }

    if (roundWon) {
        message.textContent = `Player ${currentPlayer} wins!`;
        winSound.play();
        updateScore();
        gameActive = false;
        return;
    }

    if (!gameState.includes('')) {
        message.textContent = 'Game ended in a draw!';
        gameActive = false;
        return;
    }

    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    currentPlayerDisplay.textContent = currentPlayer;
}

function highlightWinningCells(a, b, c) {
    cells[a].classList.add('winning');
    cells[b].classList.add('winning');
    cells[c].classList.add('winning');
}

function updateScore() {
    if (currentPlayer === 'X') {
        scoreX++;
        scoreXDisplay.textContent = scoreX;
    } else {
        scoreO++;
        scoreODisplay.textContent = scoreO;
    }
}

function resetGame() {
    gameActive = true;
    currentPlayer = 'X';
    gameState = ['', '', '', '', '', '', '', '', ''];
    message.textContent = '';
    currentPlayerDisplay.textContent = currentPlayer;

    cells.forEach(cell => {
        cell.textContent = '';
        cell.classList.remove('winning');
    });
}

cells.forEach(cell => cell.addEventListener('click', handleCellClick));
resetButton.addEventListener('click', resetGame);
currentPlayerDisplay.textContent = currentPlayer;