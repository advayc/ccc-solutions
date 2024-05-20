import sys
input = sys.stdin.readline
n, q = map(int, input().split())
eps = list(map(int, input().split()))

# Compute prefix sums
prefix_sums = [0] * (n + 1)
for i in range(n):
    prefix_sums[i + 1] = prefix_sums[i] + eps[i]

results = []
for _ in range(q):
    c, e = map(int, input().split())
    # Calculate the sum of episodes outside the range [c, e]
    sum_outside = prefix_sums[c - 1] + (prefix_sums[n] - prefix_sums[e])
    results.append(sum_outside)

for result in results:
    print(result)
2
abc
aaa