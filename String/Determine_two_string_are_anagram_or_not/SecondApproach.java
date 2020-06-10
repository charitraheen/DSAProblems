import java.util.HashMap;
import java.util.Map;

class SecondApproach {
	// Function to check if X and Y are anagrams or not
	public static boolean isAnagram(String X, String Y) {
		// if X's length is not same as Y's, they can't be anagram
		if (X.length() != Y.length()) {
			return false;
		}

		// create an empty map
		Map<Character, Integer> freqX = new HashMap<>();

		// maintain count of each character of X in the map
		for (char c: X.toCharArray()) {
			freqX.put(c, freqX.getOrDefault(c, 0) + 1);
		}

		// create a second map
		Map<Character, Integer> freqY = new HashMap<>();

		// maintain count of each character of Y in the map
		for (char c: Y.toCharArray()) {
			freqY.put(c, freqY.getOrDefault(c, 0) + 1);
		}

		// return true if both map has same content
		return freqX.equals(freqY);
	}

	public static void main(String[] args) {
		String X = "tommarvoloriddle";	// Tom Marvolo Riddle
		String Y = "iamlordvoldemort";	// I am Lord Voldemort

		if (isAnagram(X, Y)) {
			System.out.println("Anagram");
		} else {
			System.out.println("Not a Anagram");
		}
	}
}
