def permute(nums: list):
    result = []

    if len(nums) == 1: # base case
        return [nums[:]] # returns a list of [1]
    
    for i in range(len(nums)):#loop through the nums array 
        n=nums.pop(0) # take away 0th index so now [1,2,3] = [2,3], [3,2]

        perms = permute(nums)# calls function recursivly
        
        for perm in perms:
            perm.append(n)

        result.extend(perms)
        nums.append(n)
    return result

nums = list(map(int, input().split()))
print(permute(nums))