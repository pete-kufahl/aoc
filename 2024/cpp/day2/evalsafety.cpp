#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

bool check_line(vector<int>& levels, int lo, int hi) {
    // track monotonicity direction
    bool mono_known = false;
    bool increasing = false;

    for (int i = 1; i < levels.size(); i++) {
        int diff = levels[i] - levels[i -1];
        // check difference against bounds
        if (abs(diff) < lo || abs(diff) > hi) return false;

        // check monotonicity; handle unknown case
        if (!mono_known) {
            if (diff != 0) { 
                increasing = diff > 0;
                mono_known = true;
            }
        } else {
            if ((increasing && diff < 0) || (!increasing && diff > 0)) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    // params
    int lo = 1;
    int hi = 3;

    // tracking
    int safe_lines = 0;
    int safe_lines_modified = 0;

    ifstream inputFile("input.txt");
    if (!inputFile) {
        cerr << "Error: Unable to open file input.txt" << endl;
        return 1;
    }
    string line;
    while (getline(inputFile, line)) {
        istringstream lineStream(line);
        vector<int> levels;
        int value;

        // parse an unknown number of integers from the current line
        // std::istringstream automatically skips whitespace
        while (lineStream >> value) {
            levels.push_back(value);
        }
        if (levels.size() > 1) {
            if (!check_line(levels, lo, hi)) {
                // create sublists and check them for safety
                for (size_t i = 0; i < levels.size(); ++i) {
                    vector<int> sublist;
                    for (size_t j = 0; j < levels.size(); j++) {
                        if (j != i) {
                            sublist.push_back(levels[j]);
                        }
                    }
                    if (check_line(sublist, lo, hi)) {
                        safe_lines_modified += 1;
                        break;
                    }
                }
            } else {
                safe_lines += 1;
            }
        }
    }
    int total_safe = safe_lines + safe_lines_modified;
    cout << safe_lines << " lines of safe levels (without modification" << endl;
    cout << total_safe << " lines of safe levels (allowing 1 level to be disregarded)" << endl;
}

/*
* > clang --version
* > clang++ -std=c++17 evalsafety.cpp -o exec/evalsafety
* > exec/evalsafety
*/