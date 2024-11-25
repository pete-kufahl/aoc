/*
Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
PART 1: To what floor do the instructions take Santa?

Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
PART 2: What is the position of the character that causes Santa to first enter the basement?
*/

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
