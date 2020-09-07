class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        answer = 0 
        
        prev = 0
        
        for i in range(1, len(s)):
            if s[i] != s[prev]:
                prev = i
            else:
                answer += min(cost[i], cost[prev])
                if cost[prev] < cost[i]: prev = i    ## case to handle with thre or more consective char
        return answer
