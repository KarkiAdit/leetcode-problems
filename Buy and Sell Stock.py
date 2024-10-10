# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_list = [prices[0]]
        max_list = [prices[-1]]
        for idx in range(1, len(prices)):
            min_list.append(min(prices[idx], min_list[idx - 1]))
            max_list.append(max(prices[len(prices) - idx - 1], max_list[idx - 1]))
        max_sell_price = 0
        for idx in range(len(max_list) - 1):
            curr_max_value = max_list[len(prices) - idx - 2] - min_list[idx]
            max_sell_price = max(max_sell_price, curr_max_value)
        return max_sell_price
        
        
        
    