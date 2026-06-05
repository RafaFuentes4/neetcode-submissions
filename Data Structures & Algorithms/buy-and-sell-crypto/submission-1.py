"""
    Input: prices = [10,1,5,6,7,1]
    Output: 6
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        l = 0
        
        max_profit = 0
        for current_price in prices[1:]:
            if current_price < min_price:
                min_price = current_price
            else:
                current_profit = current_price - min_price
                max_profit = max(max_profit, current_profit) 

        return max_profit



        