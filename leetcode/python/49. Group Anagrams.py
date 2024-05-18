class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total = defaultdict(list)
        for s in strs:
            c = [0]*26

            for count in s:
                c[ord(count)- ord('a')]+=1

            total[tuple(c)].append(s)
        return total.values()