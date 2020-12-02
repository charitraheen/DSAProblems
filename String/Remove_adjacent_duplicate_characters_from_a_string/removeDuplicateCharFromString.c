#include <stdio.h>
#include <stdlib.h>

// Function to remove adjacent duplicates characters from a string
void removeDuplicates(char S[]) {
	int n = strlen(S);
	char prev = '\0';
	int k = 0;

	// loop through the string
	for (int i = 0; i < n; i++) {
		// if current characters is different than the previous char
		if (prev != S[i]) {
			// set distinct chars at index k and increment it 
			S[k++] = S[i];
		}
		// update previous char to current char for next iteration of loop
		prev = S[i];
	}
	// null terminate the resultant string
	S[k] = '\0';
}

int main(void) {
	char S[] = "AAABBCDDD";
	removeDuplicates(S);

	printf("%s", S);

	return 0;
}
