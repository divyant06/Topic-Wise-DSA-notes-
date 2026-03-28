# 1. Recursive Factorial 
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 2. Fibonacci (The slow naive way)
# This one is O(2^n) because it repeats work
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# 3. Fibonacci (Memoized version)
# Much faster O(n) using a dictionary to save results
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# 4. Tower of Hanoi
# n = disks, s = source, t = target, a = auxiliary
def hanoi(n, s, t, a):
    if n > 0:
        hanoi(n - 1, s, a, t)
        print(f"Move disk {n} from {s} to {t}")
        hanoi(n - 1, a, t, s)

# 5. Recursive Binary Search 
# Logic: cut the list in half every time
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
            
    return -1 

# Execution
if __name__ == "__main__":
    
    print("Factorial of 5:", factorial(5))
    
    print("\nFibonacci Comparison:")
    print("Naive (n=10):", fib_naive(10))
    print("Memoized (n=10):", fib_memo(10))
    
    print("\nTower of Hanoi Trace (N=3):")
    hanoi(3, 'A', 'C', 'B')
    
    data = [10, 20, 30, 40, 50]
    target_val = 40
    print(f"\nSearching for {target_val} in {data}...")
    res = binary_search(data, 0, len(data)-1, target_val)
    print("Found at index:", res)
    