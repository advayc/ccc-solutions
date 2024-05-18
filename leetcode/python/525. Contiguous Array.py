class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        d[0] = -1
        max_len = 0
        running_sum = 0

        for i in range(len(nums)):
            running_sum += nums[i] if nums[i] == 1 else -1
            if running_sum in d:
                max_len = max(max_len, i - d[running_sum])
            else: 
                d[running_sum] = i

        return max_len