#include <iostream>
#include <fstream>
#include <stdexcept>  // For throwing exceptions
#include <utility>    // For std::pair
#include <set>        // For std::set

std::pair<int, int> moveDirection(char direction, int x, int y) {
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
            throw std::invalid_argument("Invalid direction: " + std::string(1, direction));  // Throw exception for invalid direction
    }
    // Return the updated coordinates as a pair
    return std::make_pair(x, y);
}

int main() {
    std::ifstream file("input.txt");

    if (!file.is_open()) {
        std::cerr << "Error: Could not open file." << std::endl;
        return 1;
    }
    int moves = 0;
    int x = 0, y = 0;

    // Create a set to store unique coordinates (visited positions)
    std::set<std::pair<int, int>> visited;

    // Add the initial starting position to the set
    visited.insert(std::make_pair(x, y));

    char ch;
    while (file.get(ch)) {
        moves += 1;

        // Get new coordinates after moving
        std::pair<int, int> newCoordinates = moveDirection(ch, x, y);

        // Update the current position
        x = newCoordinates.first;
        y = newCoordinates.second;

        // Insert the new coordinates into the visited set
        visited.insert(newCoordinates);
    }
    std::cout << "after " << moves << " moves, " << visited.size() << " houses were visited" << std::endl;
    file.close();
    return 0;
}