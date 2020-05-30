import java.util.Arrays;

class UsingSorting {
	// Naive method to find a pair in an array with given sum
	public static void findPair(int[] A, int sum) {
		// Sort the array in ascending order
		Arrays.sort(A);

		// Maintain two indices pointing to end-points of the array
		int low = 0;
		int high = A.length - 1;

		// Reduce search space arr[low..high] at each iteration of the loop
		// Loop till low is less than high
		while (low < high) {
			if (A[low] + A[high] == sum) {
				System.out.println("Pair found");
				return;
			}

			// Increment low index if total is less than the desired sum
			// Decrement high index is total is more than the sum
			if (A[low] + A[high] < sum) {
				low++;
			} else {
				high--;
			}
		}
		// No pair with given sum exists in the array
		System.out.println("Pair not found");
	}

	// Find pair with given sum in the array
	public static void main(String[] args) {
		int[] A = {8, 7, 2, 5, 3, 1};
		int sum = 10;

		findPair(A, sum);
	}
}
