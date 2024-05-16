#include <iostream>
#include <vector>
using namespace std;

void generateSubsets(vector<int>& nums, vector<int>& current, int index) {
    // Base case: Print the current subset
    for (int num : current)
        cout << num << " ";
    cout << endl;

    // Explore choices for the next element
    for (int i = index; i < nums.size(); ++i) {
        current.push_back(nums[i]);
        generateSubsets(nums, current, i + 1);
        current.pop_back(); // Backtrack
    }
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<int> current;
    generateSubsets(nums, current, 0);
    return 0;
}

// backtracking to find all subsets of a given set