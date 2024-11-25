// > cargo new day1
// > (move sl input.txt into day1/)
// > cargo run
use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() {
    let file = File::open("input.txt").expect("File not found");
    let reader = BufReader::new(file);

    let mut char_count = 0;
    let mut floor = 0;
    let mut basement_found = false;

    for line in reader.lines() {
        let line = line.unwrap();
        for c in line.chars() {
            char_count += 1;
            if c == '(' {
                floor += 1;
            } else if c == ')' {
                floor -= 1;
                if !basement_found && floor < 0 {
                    basement_found = true;
                    println!("Basement found at character {}", char_count);
                }
            }
        }
    }

    println!("Total characters: {}", char_count);
    println!("Ends on floor: {}", floor);
}