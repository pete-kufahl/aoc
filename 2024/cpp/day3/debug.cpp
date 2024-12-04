#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <regex>

int main() {
    // Example input string for testing
    std::string input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";
    // "do() don't()";

    // Define regex patterns
    std::regex doPattern(R"(do\(\))");
    std::regex dontPattern(R"(don't\(\))");

    // Match "do()"
    std::smatch match;
    if (std::regex_search(input, match, doPattern)) {
        std::cout << "Matched 'do()' at position: " << match.position() << std::endl;
    } else {
        std::cout << "No match for 'do()'" << std::endl;
    }

    // Match "don't()"
    if (std::regex_search(input, match, dontPattern)) {
        std::cout << "Matched 'don't()' at position: " << match.position() << std::endl;
    } else {
        std::cout << "No match for 'don't()'" << std::endl;
    }

    return 0;
}
