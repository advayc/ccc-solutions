class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        low=0
        high=len(nums)-1
        if target in nums:
            while high > low:
                middle = (high + low)//2
                if nums[middle] < target:
                    low = middle+1
                else:
                    high = middle
            return low
        else:
            return -1