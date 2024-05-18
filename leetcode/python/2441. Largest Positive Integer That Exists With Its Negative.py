class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] >= 0:
            return -1
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] >= 0:
                return -1
            if nums[i]*-1 == nums[j]:
                return nums[j]
            if nums[i]*-1 < nums[j]:
                j-=1
            else:
                i+=1
        return -1