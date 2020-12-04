#include <iostream>
#include <numeric>
using namespace std;

// Find missing number in a limited range array [1.. n+1]
int findMissingElement(int A[], int n) {
	// calculate sum of all elements of the array A
	int sum = accumulate(A, A + n, 0);
	// expected sum - actual sum
	return (n + 1) + n * (n + 1) / 2 - sum;
}

int main() {
	// input array contains n numbers between [1 to n+1]
	// with one number missing and no duplicates
	int A[] = { 3, 2, 4, 6, 1 };
	int n = sizeof(A)/sizeof(A[0]);

	cout << "The missing element is " << findMissingElement(A, a);

	return 0;
}
