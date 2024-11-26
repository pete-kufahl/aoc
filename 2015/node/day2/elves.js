const fs = require('fs');
const readline = require('readline');

// Function to read file line by line
function readFileLineByLine(filePath) {
    // Create a readable stream from the file
    const fileStream = fs.createReadStream(filePath);

    // Create a readline interface to read the file line by line
    const rl = readline.createInterface({
        input: fileStream,
        output: process.stdout,
        terminal: false
    });

    // tracking variables
    var i = 0
    var total_paper = 0
    var total_ribbon = 0

    // Listen for each line and process it
    rl.on('line', (line) => {
        // Split the line by 'x' and convert the parts to integers
        const [x1, x2, x3] = line.split('x').map(Number);

        if (isNaN(x1) || isNaN(x2) || isNaN(x3)) {
            console.error('Invalid input line:', line);
        } else {
            i += 1;
            // surface area of the box, which is 2*l*w + 2*w*h + 2*h*l
            const sides = [ x1 * x2, x1 * x3, x2 * x3 ];
            const surfaceArea = 2 * sides.reduce((a, b) => a+b, 0);
            const smallest = Math.min(...sides);
            total_paper += surfaceArea + smallest;

            // shortest distance around its sides, or the smallest perimeter of any one face
            const perimeters = [2 * x1 + 2 * x2, 2 * x1 + 2 * x3, 2 * x2 + 2 * x3];
            const smallestPerim = Math.min(...perimeters);
            // cubic feet of volume of the present
            const bow = x1 * x2 * x3;
            total_ribbon += smallestPerim + bow;
        }
    });

    // Handle the end of the file
    rl.on('close', () => {
        // console.log('Finished reading the file');
        console.log(`total paper needed for ${i} gifts: ${total_paper} ft^3`)
        console.log(`total ribbon needed is ${total_ribbon} ft`)
    });

    // Handle errors
    rl.on('error', (err) => {
        console.error('Error reading the file:', err);
    });
}

const filePath = 'input.txt';
readFileLineByLine(filePath);
