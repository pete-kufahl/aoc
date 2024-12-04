#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <regex>
#include <vector>
#include <algorithm>

using namespace std;

struct Event {
    string type;        // "mul", "do", or "dont"
    size_t position;    // position in the input string
    vector<int> values; // for "mul", store X and Y
};

void processEvent(const Event& event) {
    // Example processing
    cout << "Event Type: " << event.type
              << ", Position: " << event.position;

    if (event.type == "mul") {
        cout << ", Values: (" << event.values[0] << ", " << event.values[1] << ")";
    }

    cout << endl;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <1 or 2>\n";
        return 1;
    }
    int option = stoi(argv[1]);

    ifstream inputFile("input.txt");
    if (!inputFile) {
        cerr << "Error: Unable to open file input.txt" << endl;
        return 1;
    }

    // Read the entire file content and remove newlines
    ostringstream buffer;
    buffer << inputFile.rdbuf();
    string input = buffer.str();
    input.erase(remove(input.begin(), input.end(), '\n'), input.end());

    inputFile.close();

    std::regex mulPattern(R"(mul\((\d+),(\d+)\))");
    // regex doPattern(R"(do\(\))"); // regex doPattern(R"(do\(\))");
    // regex dontPattern(R"(don't\(\))"); // regex dontPattern(R"(don\'t\(\))");

    std::regex doPattern(R"(do\(\))");
    std::regex dontPattern(R"(don't\(\))");

    // Search and process patterns
    std::smatch match;
    size_t position = 0;
    bool enabled = true;
    long sum_products = 0;
    bool use_dos_donts = true;

    while (position < input.length()) {
        // Create a substring from the current position
        std::string subInput = input.substr(position);

        if (std::regex_search(subInput, match, mulPattern)) {
            // Match "mul(X,Y)"
            if (enabled) {
                cout << "mul(X, Y) at " << position << ", going to " << position + match.position() + match.length() << endl;
                sum_products += stoi(match[1]) * stoi(match[2]);
            } else {
                cout << "mul() skipped" << endl;
            }
            position += match.position() + match.length();
        } else if (std::regex_search(subInput, match, doPattern)) {
            // Match "do()"
            cout << "DO" << endl;
            if (use_dos_donts) {
                enabled = true;
            }
            position += match.position() + match.length();
        } else if (std::regex_search(subInput, match, dontPattern)) {
            // Match "don't()"
            cout << "DONT" << endl;
            if (use_dos_donts) {
                enabled = false;
            }
            position += match.position() + match.length();
        } else {
            break; // No more matches
        }
    }
    cout << "total for " << (use_dos_donts ? "part 2: " : "part1: ") << sum_products << endl;

    return 0;
}
