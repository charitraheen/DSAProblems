# Function to find All N-digit numbers with equal sum of digits at even
# And odd index in Bottom-up Manner
def findNdigitNums(n, res="", diff=0):

    # If number is less than N-digit
    if n > 0:

        ch = ord('0')

        # spacial case - number can't start from 0
        if res == "":
            ch = ord('1')

        # consider every valid digit and put it in the current 
        # index and recur for next index
        while ch <= ord('9'):

            # update difference between odd and even digits 
            if n & 1:
                # add value to diff if odd digit
                absdiff = diff + (ch - ord('0'))
            else:
                # subtract value from diff if even 
                absdiff = diff - (ch - ord('0'))

            findNdigitNums(n - 1, res + chr(ch), absdiff)
            ch += 1

    # if number becomes N-digit with equal to sum of even and odd
    # digits, print it
    elif n == 0 and abs(diff) == 0:
        print(res, end=" ")


if __name__ == "__main__":

    n = 3   # N-digit

    findNdigitNums(n)

