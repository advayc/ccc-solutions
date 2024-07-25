import time

N = int(input())
start_time = time.time()
dp = [0] * N

# redefine first two elements in the array to be 1 and 1 as they are your base cases
dp[0], dp[1] = 1, 1

for i in range(2, N):
    dp[i] = dp[i-1] + dp[i-2]

result = dp[N-1]

end_time = time.time()
execution_time = end_time - start_time
print(f"The Fibonacci number at position {N} is {result}")
print(f"Execution time: {execution_time} seconds")
# iteratively compute each Fibonacci number from the bottom up. This approach avoids the need for recursion and memoization.

# fib(1), fib(2), fib(3) get saved as base cases in the array
# this allows us to skip having to recompute them if we were using recursion