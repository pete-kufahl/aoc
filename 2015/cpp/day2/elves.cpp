#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int computePaper(int a, int b, int c) {
    // surface area of the box, which is 2*l*w + 2*w*h + 2*h*l
    vector<int> sides;
    sides.push_back(a * b);
    sides.push_back(b * c);
    sides.push_back(c * a);
    int surfaceArea = 2 * (sides[0] + sides[1] + sides[2]);
    // the area of the smallest side
    // need to derefence
    int minArea = *min_element(sides.begin(), sides.end());
    return surfaceArea + minArea;
}

int computeRibbon(int a, int b, int c) {
    // shortest distance around its sides, or the smallest perimeter of any one face
    vector<int> perimeters;
    perimeters.push_back(2 * (a + b));
    perimeters.push_back(2 * (a + c));
    perimeters.push_back(2 * (b + c));
    int smallestSide = *min_element(perimeters.begin(), perimeters.end());
    // cubic feet of volume of the present
    int bow = a * b * c;
    return smallestSide + bow;
}

int main() {
    string filename = "input.txt";
    ifstream file(filename);

    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        return 1;
    }

    string line;
    int gifts = 0;
    int totalPaper = 0;
    int totalRibbon = 0;

    while (getline(file, line)) {
        stringstream ss(line);
        string part;
        vector<int> dims;

        // Read and parse the line into three integers
        while (getline(ss, part, 'x')) {
            dims.push_back(stoi(part));  // Convert string to integer and store in vector
        }

        if (dims.size() == 3) {
            gifts += 1;
            int a = dims[0];
            int b = dims[1];
            int c = dims[2];

            totalPaper += computePaper(a, b, c);
            totalRibbon += computeRibbon(a, b, c);
        } else {
            cerr << "Invalid line format: " << line << endl;
        }
    }

    file.close();

    cout << "Number of Gifts: " << gifts << endl;
    cout << "Total Paper: " << totalPaper << endl;
    cout << "Total Robbon: " << totalRibbon << endl;

    return 0;
}
