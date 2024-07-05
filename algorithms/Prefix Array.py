nums=[1,2,3,4,5,6]
n = len(nums)
prefix=[0 for i in range(n)]
prefix[0]=nums[0]
for i in range(1,n):
    prefix[i] = prefix[i-1]+nums[i]
print(prefix)