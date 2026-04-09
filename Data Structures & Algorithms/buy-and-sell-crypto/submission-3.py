class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        1. Initialize max_profit as 0
        2. Initialize i = 0 , j = 1
        3. While i< j , check max(difference(prices[j], prices[i]))
        4. If it is greater than max_profit, replace max_profit with it. 
        5. Continue till the end and return max_profit
        '''
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit


