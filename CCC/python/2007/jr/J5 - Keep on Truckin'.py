motels=[0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
mini = int(input())
maxi = int(input())
n = int(input())
for i in range(n):
    additional=int(input())
    motels.append(additional)
motels.sort()
num = len(motels)
dp = [0] * num
dp[0] = 1 # already there so one
for i in range(num):
    for j in range(i+1, num):
        distance = motels[j] - motels[i]
        if mini <= distance <= maxi:
            dp[j] += dp[i]   

print(dp[num-1])
