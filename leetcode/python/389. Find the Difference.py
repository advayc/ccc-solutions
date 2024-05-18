class Solution(object):
    def findTheDifference(self, s, t):
        sum = 0
        for c in t:
            sum = (sum + ord(c)) % 256
        for c in s:
            sum = (sum - ord(c)) % 256
        return chr(sum)