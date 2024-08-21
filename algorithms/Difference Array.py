nums=[1,2,3,4,5,6]
n = len(nums)
diff=[0 for _ in range(n)]
for i in range(n, 0, -1):
    diff[i]=diff[i]-diff[i-1]

print(diff)
