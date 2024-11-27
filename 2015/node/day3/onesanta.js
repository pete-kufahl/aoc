const fs = require('fs');

function moveDirection(direction, x, y) {
    switch (direction) {
        case '<': // Move left
            x -= 1;
            break;
        case '>': // Move right
            x += 1;
            break;
        case '^': // Move up
            y += 1;
            break;
        case 'v': // Move down
            y -= 1;
            break;
        default:
            throw new Error("Invalid direction: " + direction);
    }
    return [x, y];
}

function readFile(filePath) {
    const fileStream = fs.createReadStream(filePath);
    var moves = 0;
    var santa = [0, 0];
    let visited = new Set();
    visited.add(JSON.stringify(santa));

    fileStream.on('data', (chunk) => {
        for (let i = 0; i < chunk.length; i++) {
            moves += 1;
            const char = String.fromCharCode(chunk[i]); // Convert the byte to a string
            santa = moveDirection(char, santa[0], santa[1]);
            visited.add(JSON.stringify(santa));
        }
        console.log(`after ${moves} moves, ${visited.size} houses visited`);
    });

    fileStream.on('error', (err) => {
        console.error('Error reading file:', err);
    });
}

const filePath = 'input.txt';
readFile(filePath);