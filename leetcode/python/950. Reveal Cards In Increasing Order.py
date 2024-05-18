class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
        n = len(deck)
        result = [0] * n
        x = deque(range(n))
        
        for card in deck:
            idx = x.popleft()  
            result[idx] = card      
            if x:               
                x.append(x.popleft())  
        
        return result