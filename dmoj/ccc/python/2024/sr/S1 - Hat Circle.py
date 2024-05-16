N = int(input())
hats = [int(input()) for _ in range(N)]

same_hat_count = 0
for i in range(N//2):
    if hats[i] == hats[i+N//2]:
        same_hat_count += 2

print(same_hat_count)
