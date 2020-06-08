# Recursive function to check if str[low..high] is palindrome or not
def isPalindrome(str, low, high):
    return (low >= high) or (str[low] == str[high] and isPalindrome(str, low + 1, high - 1))

# Function to check if given string is a rotated palindrome or not
def isRotatedPalindrome(str):

    # length of the given string
    m = len(str)

    # check for all rotations of the given string if it is palindrome or not
    for i in range(m):

        # in-place rotate the string by 1 unit 
        str = str[1:] + str[0]

        # return true the string is a palindrome
        if isPalindrome(str, 0, m - 1):
            return True

    # return false if no rotation is a palindrome
    return false

# Check if given string is a rotated palindrome or not
if __name__ == "__main__":

    # palindrome string
    str = "ABCDCBA"

    # rotate it by 2 units
    str = str[2:] + str[:2]

    if isRotatedPalindrome(str):
        print("Yes")
    else:
        print("No")
