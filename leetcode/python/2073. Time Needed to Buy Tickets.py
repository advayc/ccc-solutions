class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c=0
        for i in range(len(tickets)):
            if i <=k:
                c+=min(tickets[i], tickets[k])
            else:
                c+= min(tickets[i], tickets[k] -1)
        return c