
naive_calls = 0 

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n
    
    return fib_naive(n-1) + fib_naive(n-2)


# Memoized Fibonacci
memo_calls = 0

def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]



# Main Execution

n = int(input("Enter value of n: "))

# Reset counters
naive_calls = 0
memo_calls = 0

print("--- Naive Fibonacci ---")
result_naive = fib_naive(n)
print("Fibonacci Value:", result_naive)
print("Naive Function Calls:", naive_calls)

print("--- Memoized Fibonacci ---")
result_memo = fib_memo(n)
print("Fibonacci Value:", result_memo)
print("Memoized Function Calls:", memo_calls)

print("Time Complexity:")
print("Naive Fibonacci → O(2^n)")
print("Reason: Repeated subproblems")

print("Memoized Fibonacci → O(n)")
print("Reason: Each value computed only once")

print("Space Complexity:")
print("Naive → O(n) (recursion stack)")
print("Memoized → O(n) (recursion stack + memo storage)")