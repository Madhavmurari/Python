class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[float('inf') for i in range(amount+1)]
        dp[0]=0
        for coin in coins:
            for amo in range(coin,amount+1):
                dp[amo]=min(dp[amo],dp[amo-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1

        
        