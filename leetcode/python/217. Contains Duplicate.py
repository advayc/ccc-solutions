class Solution:
    def containsDuplicate(self, nums: List[int]):
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
        