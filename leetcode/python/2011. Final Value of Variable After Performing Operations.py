class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum=0
        for i in operations:
            if i in {'X--', '--X'}:
                sum-=1
            elif i in {'X++', '++X'}:
                sum+=1
        return sum