def hasDuplicates(A, k):
    # stores (element, index) pairs as (key, value) pairs 
    dict = {}

    # traverse the list
    for i, e in enumerate(A):
        # if the element already exists in the dict
        if e in dict:
            # return true if the current element is  repeated within range of k 
            if i - dict.get(e) <= k:
                return True

        # store elements along with their indices
        dict[e] = i

    # we reach here when no element  is repeated within range k 
    return False

if __name__ == "__main__":
    A = [5, 6, 8, 2, 4, 6, 9]
    k = 4

    if hasDuplicates(A, k):
        print("Duplicates found")
    else:
        print("No duplicates found")


