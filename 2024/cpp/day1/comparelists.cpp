/*
* > clang --version
* > clang++ -std=c++17 comparelists.cpp -o exec/comparelists
* > exec/comparelists
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <unordered_set>
#include <unordered_map>

using namespace std;

long totalDifferences(vector<int>& arr1, vector<int>& arr2) {
    // Calculate the total of absolute differences
    sort(arr1.begin(), arr1.end());
    sort(arr2.begin(), arr2.end());

    int totalDifference = 0;
    for (size_t i = 0; i < arr1.size(); ++i) {
        totalDifference += abs(arr1[i] - arr2[i]);
    }
    return totalDifference;
}

long similarityOfLists(const vector<int>& arr1, const vector<int>& arr2) {
    long score = 0;

    // Create a set of unique elements in arr1
    unordered_set<int> set1(arr1.begin(), arr1.end());

    // Count occurrences of elements in arr1 that are in set1
    unordered_map<int, int> counts1;
    for (int e : arr1) {
        if (set1.count(e)) {
            counts1[e]++;
        }
    }

    // Count occurrences of elements in arr2 that are in set1
    std::unordered_map<int, int> counts2;
    for (int e : arr2) {
        if (set1.count(e)) {
            counts2[e]++;
        }
    }

    // Calculate similarity score
    for (int a : set1) {
        score += static_cast<long>(a) * counts1[a] * counts2[a];
    }
    return score;
}

int main() {
    ifstream inputFile("input.txt");
    if (!inputFile) {
        cerr << "Error: Unable to open file input.txt" << endl;
        return 1;
    }

    vector<int> arr1;
    vector<int> arr2;

    string line;
    while (getline(inputFile, line)) {
        // using std::istringstream to parse each line into two integers
        // std::istringstream automatically skips whitespace
        istringstream lineStream(line);
        int num1, num2;
        if (lineStream >> num1 >> num2) {
            arr1.push_back(num1);
            arr2.push_back(num2);
        }
    }

    inputFile.close();

    long totalDifference = totalDifferences(arr1, arr2);
    cout << "Total of absolute differences: " << totalDifference << endl;

    long score = similarityOfLists(arr1, arr2);
    cout << "Similarity score: " << score << endl;

    return 0;
}
