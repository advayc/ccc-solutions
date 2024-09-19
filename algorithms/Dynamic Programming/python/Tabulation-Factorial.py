import time

N = int(input('factorial of: '))
start_time = time.time()
dp = [0] * (N+1)

dp[0], dp[1], dp[2] = 0, 1, 2

for i in range(3, N+1):
    dp[i] = i * dp[i-1]

result = dp[-1]

end_time = time.time()
execution_time = end_time - start_time
print(f"{N} factorial is {result}")
print(f"Execution time: {execution_time} seconds")