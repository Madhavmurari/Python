class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit=0
        n=len(prices)
        
        mini=prices[0]
        for i in range(1,n):
            cost=prices[i]-mini
            max_profit=max(max_profit,cost)
            mini=min(mini,prices[i])
        return max_profit