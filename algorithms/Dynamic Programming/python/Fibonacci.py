import time
start_time = time.time()
end_time = time.time()
execution_time = end_time - start_time

N = int(input())
dp = [0] * N

# redefine first two elements in the array to be 1 and 1 as they are your base cases
dp[0], dp[1] = 1, 1

for i in range(2, N):
    dp[i] = dp[i-1] + dp[i-2]

result = dp[N-1]
for i in range(N):
    for j in range(i+1, N):
        res = dp[j]

print(f"The Fibonacci number at position {N} is {result}")
print(f"Execution time: {execution_time} seconds")