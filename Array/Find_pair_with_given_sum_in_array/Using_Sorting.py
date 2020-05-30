# Naive method to find a pair in a list with given sum
def find_pair(A, sum):
    
    # Sort the list in ascending order
    A.sort()
    
    # Maintain two indices pointing to end-points of the list
    (low, high) = (0, len(A) - 1)

    # Reduce search space A[low..high] at each iteration of the loop
    # Loop till low is less than high

    while low < high:
        if A[low] + A[high] == sum:
            print("Pair found")
            return 

        # Increment low index if total is less than the desired sum
        # Decrement high index if total is more than the sum
        if A[low] + A[high] < sum:
            low = low + 1
        else:
            high = high - 1

        # No pair with given sum exists in the list
        print("Pair now found")

    if __name__ == "__main__":
        A = [8, 7, 2, 5, 3, 1]
        sum = 10

        find_pair(A, sum)
