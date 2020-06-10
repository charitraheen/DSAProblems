# Function to check if X and Y are anagram or not
def isAnagram(X, Y):

    # if X's length is not same as Y's, they can't be anagram 
    if len(X) != len(Y):
        return False

    # create an empty dict
    freqX = {}
    freqY = {}

    # Maintain count of each character of X in the dict
    for i in range(len(X)):
        freqX[X[i]] = freqX.get(X[i], 0) + 1

    # Maintain count of each character of Y in the dict
    for i in range(len(Y)):
        freqY[Y[i]] = freqY.get(Y[i], 0) + 1

    # return true if both dict have same content
    return freqX == freqY

if __name__ == "__main__":

    X = "silent"
    Y = "listen"

    if isAnagram(X, Y):
        print("Anagram")
    else:
        print("Not an Anagram")

