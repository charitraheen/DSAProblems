# find missing number in a limited range list [1 to n+1]
def findMissingElement(A):
    n = len(A)
    # calculate sum of all element of the list A
    total = sum(A)

    # expect sum - actual sum
    return (n + 1) + n * (n + 1) // 2 - total

if __name__ == "__main__":
    # input list contains n numbers between [1 to n + 1]
    # with one number missing and no duplicates
    A = [3, 2, 4, 6, 1]
    print("The missing element is ", findMissingElement(A))
