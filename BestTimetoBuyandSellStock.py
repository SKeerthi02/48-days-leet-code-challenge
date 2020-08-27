
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0
        
        for i in range(len(prices)):
            compare = prices[i] - prices[left]
            if compare > maxProfit:
                maxProfit = compare
            
            if prices[i] < prices[left]:
                left = i
        
        return maxProfit
