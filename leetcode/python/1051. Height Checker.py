class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        c=0
        for i in range(len(heights)):
            if heights[i] != exp[i]:
                c+=1
        return c
