# include<stdio.h>

// Naive method to find a pair in an array with given sum
void find_pair(int arr[], int n, int sum) {

	// Consider each element except last element
	for (int i = 0; i < n - 1; i++) {

		// Start from i'th element till last element
		for (int j = i + 1; j < n; j++) {

			// If desired sum is found, print it and return
			if (arr[i] + arr[j] == sum) {
				printf("Pair found at index %d and %d", i, j);
				return;
			}
		}
	}

	// No pair with given sum exists in the array
	printf("Pair not found");
}

// Find pair with given sum in the array
int main() {
	
	int arr[] = {8, 7, 2, 5, 3, 1};
	int sum = 10;

	int n = sizeof(arr)/sizeof(arr[0]);

	find_pair(arr, n, sum);

	return 0;
}
