# Function to check if X and Y are anagrams or not
def isAnagram(X, Y):

    # if X's length is not same as Y's, they can't be anagram
    if len(X) != len(Y):
        return False

    # Create an empty dictionary
    freq = {}

    # Maintain count of each character of X in the dict
    for i in range(len(X)):
        freq[X[i]] = freq.get(X[i], 0) + 1

    # Do for each character of Y
    for i in range(len(Y)):

        # if y is not found in dict i. e. either y is not present
        # in X or has more occurrences in Y
        if not Y[i] in freq:
            return False


        # decrease the frequency of y in the dict
        freq[Y[i]] = freq[Y[i]] - 1

        # if its frequency becomes 0, erase it from dict
        if freq[Y[i]] == 0:
            del freq[Y[i]]

    # return true if dict becomes empty
    return not freq


if __name__ == "__main__":

    X = "listen"
    Y = "silent"

    if isAnagram(X, Y):
        print("Anagram")
    else:
        print("Not an Anagram")
