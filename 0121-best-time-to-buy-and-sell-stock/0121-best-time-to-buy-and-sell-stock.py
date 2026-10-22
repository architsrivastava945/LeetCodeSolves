class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        min_price_so_far = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            # Is today's price a new minimum?
            min_price_so_far = min(min_price_so_far, prices[i])
            
            # What's the potential profit if we sell today?
            potential_profit = prices[i] - min_price_so_far
            
            # Is that a new maximum profit?
            max_profit = max(max_profit, potential_profit)
            
        return max_profit