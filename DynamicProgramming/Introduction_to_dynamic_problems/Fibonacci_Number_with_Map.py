# Function to find nth Fibonacci number
def fib(n, lookup):

    if n <= 1:
        return n

    # If sub-problem is seen for the first time
    if n not in lookup:
        val = fib(n - 1, lookup) + fib(n - 2, lookup)
        lookup[n] = val

    return lookup[n]


if __name__ == "__main__":

    n = 8
    lookup = {}

    print(fib(n, lookup))
