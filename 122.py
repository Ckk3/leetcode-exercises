from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        
        for price in prices:
            if price > min_price:
                max_profit += price - min_price
                min_price = price
            min_price = min(min_price, price)
            
        return max_profit
        

        
        
        

test_class = Solution()
print(test_class.maxProfit(prices=[7,1,5,3,6,4]))
print(test_class.maxProfit(prices=[1,2,3,4,5]))
print(test_class.maxProfit(prices=[7,6,4,3,1]))
