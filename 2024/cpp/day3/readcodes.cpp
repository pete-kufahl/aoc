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
    int x = 0;          // Used only for 'mul' pattern
    int y = 0;

    // Constructor for 'do()' and 'don't()' events
    Event(size_t pos, const string& t) : position(pos), type(t) {}

    // Constructor for 'mul(X,Y)' event
    Event(size_t pos, int xVal, int yVal) : position(pos), type("mul"), x(xVal), y(yVal) {}
};

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

    regex mul_pattern(R"(mul\((\d+),(\d+)\))");
    regex do_pattern(R"(do\(\))");
    regex dont_pattern(R"(don't\(\))");

    vector<Event> events;
    
    auto begin = input.cbegin();
    auto end = input.cend();

    // Collect 'do()' events
    // end_it points to the position after the last match, as it's constructed with sregex_iterator()
    for (sregex_iterator it(begin, end, do_pattern), end_it; it != end_it; ++it) {
        events.push_back(Event(it->position(), "do"));
    }

    // Collect 'don't()' events
    for (sregex_iterator it(begin, end, dont_pattern), end_it; it != end_it; ++it) {
        events.push_back(Event(it->position(), "don't"));
    }

    // Collect 'mul(X,Y)' events and extract X, Y values
    for (sregex_iterator it(begin, end, mul_pattern), end_it; it != end_it; ++it) {
        int x = stoi((*it)[1].str());
        int y = stoi((*it)[2].str());
        events.push_back(Event(it->position(), x, y));
    }
   
    // sort events by position 
    sort(events.begin(), events.end(), [](const Event& a, const Event& b) {
        return a.position < b.position;
    });

    // Print the events in order
    if (option == 1) {
        long sum_products = 0;
        for (const auto& event : events) {
            if (event.type == "do") {
                cout << "do() at position " << event.position << endl;
            } else if (event.type == "don't") {
                cout << "don't() at position " << event.position << endl;
            } else if (event.type == "mul") {
                cout << "mul(" << event.x << "," << event.y << ") at position " << event.position << endl;
                sum_products += event.x * event.y;
            }
        }
        cout << "total for part 1: " << sum_products << endl;
    }

    if (option == 2) {
        bool enabled = true;
        long sum_products = 0;
        for (const auto& event : events) {
            if (event.type == "do") {
                enabled = true;
            } else if (event.type == "don't") {
                enabled = false;
            } else if (enabled && event.type == "mul") {
                sum_products += event.x * event.y;
            } 
        }
        cout << "total for part 2: " << sum_products << endl;
    }
    return 0;
}
