// > node santa.js
const fs = require('fs');

function readFile(filePath) {
    const fileStream = fs.createReadStream(filePath);
    var floor = 0;
    var num = 0;
    var basement = false;

    fileStream.on('data', (chunk) => {
        for (let i = 0; i < chunk.length; i++) {
            num += 1;
            const char = String.fromCharCode(chunk[i]); // Convert the byte to a string
            if (char === '(') {
                floor += 1;
            } else if (char === ')') {
                floor -= 1;
                if (!basement && floor < 0) {
                    basement = true;
                    console.log(`basement entered at position ${num}`)
                }
            } else {
                // console.log('Character:', char);
            }
        }
    console.log(`final floor after ${num} characters is position ${floor}`);
  });

  fileStream.on('error', (err) => {
    console.error('Error reading file:', err);
  });
}

const filePath = 'input.txt';
readFile(filePath);
