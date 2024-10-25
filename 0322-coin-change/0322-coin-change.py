class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 0  # 0 coins needed to make amount 0

        for i in range(1, n + 1):
            for j in range(amount + 1):
                dp[i][j] = dp[i-1][j]  # Exclude the current coin
                
                if coins[i-1] <= j:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j - coins[i-1]])  # Include the current coin

        result = dp[n][amount]
        return result if result != float('inf') else -1




        # dp=[0]+[float('inf')]*(amount+1)  ## dp[0]=0
        
        # for coin in coins:
        #     for i in range(coin,amount+1):
        #         dp[i]=min(dp[i],dp[i-coin]+1)
        # return dp[amount] if dp[amount]!=float('inf') else -1

        
        