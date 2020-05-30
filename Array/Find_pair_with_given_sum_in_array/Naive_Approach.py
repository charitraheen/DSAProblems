# Naive method to find a pair in a list with given sum

def find_pair(A, sum):

    # consider each element except last element
    for i in range(len(A) - 1):

        # start from i'th element till last element
        for j in range(i + 1, len(A)):

            # if desired sum is found, print it and return
            if A[i] + A[j] == sum:
                print("Pair found at index", i, "and", j)
                return 

    # No pair with given sum exists in the list
    print("Pair not found")


if __name__ == "__main__":

    A = [8, 7, 2, 5, 3, 1]
    sum = 0

    find_pair(A, sum)
