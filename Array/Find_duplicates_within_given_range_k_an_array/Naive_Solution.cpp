#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

bool hasDuplicates(vector<int> &vec, int k) {
	// stores (element, index) pairs as (key, value) pairs
	unordered_map<int, int> map;

	// traverse the vector
	for (int i = 0; i < vec.size(); i++) {
		// if the current element already exists in the map
		if (map.find(vec[i]) != map.end()) {
			// return true if current element is repeated within range of k
			if (i - map[vec[i]] <= k) {
				return true;
			}
		}
		// stores elements along with their indices
		map[vec[i]] = i;
	}
	// we reach here when no element is repeated within range k
	return false;
}

int main() {
	vector<int> vec = { 5, 6, 8, 2, 4, 6, 9 };
	int k = 4;
	if (hasDuplicates(vec, k)) {
		cout << "Duplicates found";
	} else {
		cout << "No duplicates found";
	}

	return 0;
}
