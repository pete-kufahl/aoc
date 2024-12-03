const fs = require('fs');
const readline = require('readline');

function checkLine(levels, lo, hi) {
    // monotonicity direction
    let increasing = null;

    for (let i = 1; i < levels.length; i++) {
        const diff = levels[i] - levels[i - 1];

        // difference versus bounds
        if (Math.abs(diff) < lo || Math.abs(diff) > hi) {
            return false;
        }

        // determine or validate monotonicity
        if (increasing === null) {
            if (diff !== 0) {
                increasing = diff > 0;
            }
        } else {
            if ((increasing && diff < 0) || (!increasing && diff > 0)) {
                return false;
            }
        }
    }
    return true;
}

function findSafeSublist(levels, lo, hi) {
    // create 1-removed sublists and check them for safety
    // return true if ANY sublist is found to be safe
    for (let i = 0; i < levels.length; i++) {
        const sublist = levels.slice(0, i).concat(levels.slice(i + 1));
        if (checkLine(sublist, lo, hi)) {
            return true;
        }
    }
    return false;
}

function compareLists(filePath) {
    // stream, interface from file
    const fileStream = fs.createReadStream(filePath);
    const rl = readline.createInterface({
        input: fileStream,
        output: process.stdout,
        terminal: false
    });

    // data structures
    const list1 = [];
    const list2 = [];

    // tracking
    let safeLines = 0;
    let safeLinesIfModified = 0;

    // params
    const lo = 1;
    const hi = 3;

    // Listen for each line and process it
    rl.on('line', (line) => {
        // Split the line by whitespace and convert the parts to integers
        const [num1, num2] = line.trim().split(/\s+/).map(Number);
        levels = line.trim().split(/\s+/).map(Number);

        if (checkLine(levels, lo, hi)) {
            safeLines += 1;
        } else if (findSafeSublist(levels, lo, hi)) {
            safeLinesIfModified += 1;
        }
    });
    
    // Handle the end of the file
    rl.on('close', () => {
        // part 1
        console.log(`Number of safe levels: ${safeLines}`);
        // part 2
        const totalSafeLines = safeLines + safeLinesIfModified;
        console.log(`Number of safe levels, with 0 or 1 elements removed: ${totalSafeLines}`);
    });

    // Handle errors
    rl.on('error', (err) => {
        console.error('Error reading the file:', err);
    });
}


const filePath = 'input.txt';
compareLists(filePath);