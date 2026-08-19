class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum_purchase = prices[0] # keep track of cheapest item to purchase

        for coin in prices: # for every item in prices 
            minimum_purchase = min(minimum_purchase, coin) # the minimum purchase for each item
            max_profit = max(max_profit, coin - minimum_purchase) # ensures the highest profit comes from the current

        return max_profit