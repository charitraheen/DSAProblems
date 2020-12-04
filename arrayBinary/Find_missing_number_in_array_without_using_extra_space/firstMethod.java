import java.util.Arrays;

class main {
	// find missing number in a limited range array [1 to n + 1]
	public static int findMissingElement(int[] A) {
		int n = A.length();

		// Calculate sum of all element of the array A
		int sum = Arrays.stream(A).sum();

		// expected sum - actual sum
		return (n + 1) + n * (n + 1) / 2 - sum;
	}

	public static void main(String[] args) {
		// input array contains n numbers between [1 to n+1]
		// with one number missing and no duplicates
		int[] A = { 3, 2, 4, 6, 1 };
		System.out.print("The missing element is " + findMissingElement(A));
	}
}
