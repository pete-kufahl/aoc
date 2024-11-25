#include <iostream>
#include <fstream>

int process(char ch) {
    if (ch == '(') { return 1; } else if (ch == ')') { return -1; } else return 0;
}

int main() {
    std::ifstream file("input.txt");

    if (!file.is_open()) {
        std::cerr << "Error: Could not open file." << std::endl;
        return 1;
    }
    int num = 0;
    int floor = 0;
    bool basement = false;

    char ch;
    while (file.get(ch)) {
        num += 1;
        floor += process(ch);
        if (!basement && floor < 0) {
            basement = true;
            std::cout << "basement entered at position " << num << std::endl;
        }
    }
    std::cout << "final floor after " << num << " characters is " << floor << std::endl;
    file.close();
    return 0;
}