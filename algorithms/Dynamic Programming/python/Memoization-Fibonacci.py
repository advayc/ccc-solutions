import time
start_time = time.time()

def fib_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_top_down(n-1, memo) + fib_top_down(n-2, memo)
    return memo[n]

N = int(input())
result = fib_top_down(N)
end_time = time.time()
execution_time = end_time - start_time

print(f"The Fibonacci number at position {N} is {result}")
print(f"Execution time: {execution_time} seconds")
# creating the dict memo allows us to avoid redundant computations, not possible with plain recursion   