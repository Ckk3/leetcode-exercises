from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # all_options = []
        
        # current_index = 0
        # total_len_prices = len(prices)
        max_profit = 0
        min_price = prices[0]
        
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        
        #for current_index in range(total_len_prices):
            #current_price = prices[current_index]
            #for index in range(current_index + 1, total_len_prices):
                #profit_price = prices[index] - current_price
                #max_profit = max(max_profit, profit_price)
                # if profit_price > max_profit:
                    #max_profit = profit_price
            
            #current_index += 1
            #if current_index >= (total_len_prices):
                #break
        
        return max_profit
        

        
        
        

test_class = Solution()
test_class.maxProfit(prices=[list(range(10000, 0, -1))])
