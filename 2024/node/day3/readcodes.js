const fs = require('fs');
const path = require('path');

function readCodes(filePath, option) {
    const mulPattern = /mul\((\d+),(\d+)\)/g;
    const doPattern = /do\(\)/g;
    const dontPattern = /don't\(\)/g;

    // Read the file content and process it
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error(`Error reading file: ${err.message}`);
            return;
        }
        const buffer = data.replace(/\r?\n/g, '');  // remove line breaks

        const events = [];  // common container for events, to be ordered

        // Match and extract "mul(X,Y)" patterns
        let match;
        while ((match = mulPattern.exec(buffer)) !== null) {
            const x = parseInt(match[1], 10);
            const y = parseInt(match[2], 10);
            const position = match.index;
            events.push({ type: 'mul', x, y, position });
        }

        // Match and extract "do()" positions
        while ((match = doPattern.exec(buffer)) !== null) {
            const position = match.index;
            events.push({ type: 'do', position });
        }

        // Match and extract "don't()" positions
        while ((match = dontPattern.exec(buffer)) !== null) {
            const position = match.index;
            events.push({ type: 'dont', position });
        }

        // Sort events by position
        events.sort((a, b) => a.position - b.position);

        let enabled = true;  // enabled mode to start with
        let subProducts = 0;

        events.forEach((event) => {
            if (enabled && event.type === 'mul') {
                subProducts += event.x * event.y;
                // console.log(`mul(X: ${event.x}, Y: ${event.y}) at Position: ${event.position}`);
            } else if (option === 2 && event.type ==='dont') {
                enabled = false;
                // console.log(`${event.type}() at Position: ${event.position}`);
            } else if (option === 2 && event.type ==='do') {
                enabled = true;
                // console.log(`${event.type}() at Position: ${event.position}`);
            }
        });

        console.log(`total is: ${subProducts}`);
    });
}

const option = process.argv[2] && ['1', '2'].includes(process.argv[2]) ? parseInt(process.argv[2], 10) : 1;

const filePath = 'input.txt';
readCodes(filePath, option);