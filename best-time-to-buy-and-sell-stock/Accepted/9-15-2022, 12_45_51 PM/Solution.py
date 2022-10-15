// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr=prices[0]
        profit=0
        for i in range(len(prices)):
            value=prices[i]-curr
            if prices[i]<curr:
                curr=prices[i]
            if prices[i]>curr:
                if profit<value:
                    profit=value
        
        
        return profit