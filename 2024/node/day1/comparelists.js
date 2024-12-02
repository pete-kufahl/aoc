const fs = require('fs');
const readline = require('readline');

function sumDifferences(list1, list2) {
    // find differences between elements of sorted lists
    list1.sort((a, b) => a - b);
    list2.sort((a, b) => a - b);

    let totalDifference = 0;
    for (let i = 0; i < list1.length; i++) {
        totalDifference += Math.abs(list1[i] - list2[i]);
    }
    return totalDifference;
}

function similarityOfLists(list1, list2) {
    // compute similarity score
    // score contributed by each distinct element e: (value of e) * (occurrences of e in list1) * (occurrences of e in list2)
    const freq1 = {};
    const freq2 = {};

    // frequency map for list1
    list1.forEach(num => {
        freq1[num] = (freq1[num] || 0) + 1;
    });
    // frequency map for list2
    list2.forEach(num => {
        freq2[num] = (freq2[num] || 0) + 1;
    });

    let similarityScore = 0;
    for (const num in freq1) {
        if (freq2[num]) {
            similarityScore += num * freq1[num] * freq2[num];
        }
    }
    return similarityScore;
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

    // Listen for each line and process it
    rl.on('line', (line) => {
        // Split the line by whitespace and convert the parts to integers
        const [num1, num2] = line.trim().split(/\s+/).map(Number);
        // push onto sortable lists
        list1.push(num1);
        list2.push(num2);
    });
    
    // Handle the end of the file
    rl.on('close', () => {
        // console.log('Finished reading the file');
        // part 1
        const totalDifference = sumDifferences(list1, list2);
        console.log(`Total difference between lists ${totalDifference}`);
        // part 2
        const similarityScore = similarityOfLists(list1, list2);
        console.log(`Similarity score between lists is: ${similarityScore}`);
    });

    // Handle errors
    rl.on('error', (err) => {
        console.error('Error reading the file:', err);
    });
}


const filePath = 'input.txt';
compareLists(filePath);