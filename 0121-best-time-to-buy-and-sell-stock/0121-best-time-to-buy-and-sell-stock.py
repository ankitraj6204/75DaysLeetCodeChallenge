from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # best day to buy so far
        max_profit = 0            # best profit so far
        
        for price in prices:
            if price < min_price:
                min_price = price  # update buying price
            
            profit = price - min_price  # sell today
            if profit > max_profit:
                max_profit = profit
        
        return max_profit