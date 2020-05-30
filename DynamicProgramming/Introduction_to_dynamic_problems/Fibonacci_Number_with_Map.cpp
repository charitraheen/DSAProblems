#include <iostream>
#include <unordered_map>
using namespace std;

// Function to find n'th Fibonacci number
int fib(int n, auto &lookup) {
	if (n <= 1)
		return n;

	// If sub-problem is seen for the irst time
	if (lookup.find(n) == lookup.end())
		lookup[n] = fib(n - 1, lookup) + fib(n - 2, lookup);

	return lookup[n];
}

int main() {
	unordered_map<int, int> lookup;

	cout << fib(8, lookup);

	return 0;
}
