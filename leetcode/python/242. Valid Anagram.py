class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s)==sorted(t)
        #return Counter(s)==Counter(t)
        cs, ct = {}, {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            cs[s[i]] = 1+cs.get(s[i], 0) 
            ct[t[i]] = 1+ct.get(t[i], 0) 
        for c in cs:
            if cs[c]!= ct.get(c, 0):
                return False
        
        return True