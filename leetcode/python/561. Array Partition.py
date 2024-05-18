class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum=0
        while nums:
            x = nums.pop()
            y = nums.pop()
            sum+=y
        return sum