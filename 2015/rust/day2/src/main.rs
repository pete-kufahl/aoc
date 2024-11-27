use std::fs::File;
use std::io::{BufReader, BufRead};

fn compute_paper(a: i32, b: i32, c: i32) -> i32 {
    // Calculate the areas of the three sides of the box
    let sides = vec![a * b, b * c, c * a];

    // Surface area of the box: 2 * (l*w + w*h + h*l)
    let surface_area = 2 * (sides[0] + sides[1] + sides[2]);

    // Find the area of the smallest side
    let min_area = *sides.iter().min().unwrap();

    // Return the total paper required: surface area + smallest side area
    surface_area + min_area
}

fn compute_ribbon(a: i32, b: i32, c: i32) -> i32 {
    // Calculate the perimeters of the three faces of the box
    let perimeters = vec![2 * (a + b), 2 * (a + c), 2 * (b + c)];

    // Find the smallest perimeter (the shortest distance around the sides)
    let smallest_side = *perimeters.iter().min().unwrap();

    // Calculate the cubic feet (volume) of the box
    let bow = a * b * c;

    // Return the total ribbon length: smallest perimeter + volume
    smallest_side + bow
}

fn main() {
    let file = File::open("input.txt").expect("File not found");
    let reader = BufReader::new(file);

    let mut gifts = 0;
    // let mut dimensions = Vec::new();
    let mut total_paper = 0;
    let mut total_ribbon = 0;

    for line in reader.lines() {
        let line = line.unwrap();
        
        // Split the line by 'x' and parse the numbers
        let parts: Vec<i32> = line.split('x')
            .filter_map(|part| part.trim().parse().ok())  // Convert parts to integers
            .collect();

        // Ensure we have exactly three numbers
        if parts.len() == 3 {
            gifts += 1;
            let (a, b, c) = (parts[0], parts[1], parts[2]);
            // dimensions.push((a, b, c));  // Store the tuple of dimensions
            total_paper += compute_paper(a, b, c);
            total_ribbon += compute_ribbon(a, b, c);
        } else {
            eprintln!("Skipping line: Expected 3 values but found {:?}", parts);
        }
    }
    println!("Total gifts: {}", gifts);
    println!("Total paper: {} ft^3", total_paper);
    println!("Total ribbon: {} ft", total_ribbon);
}
