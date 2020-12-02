# Function to remove adjacent duplicates char from a string
def removeDuplicates(S):
    chars = list(S)
    prev = None
    k = 0

    for c in S:
        if prev != c:
            chars[k] = c
            prev = c
            k = k + 1
    return "".join(chars[:k])


if __name__ == "__main__":
    S = "AAABBCCDDD"

    S = removeDuplicates(S)

    print(S)
