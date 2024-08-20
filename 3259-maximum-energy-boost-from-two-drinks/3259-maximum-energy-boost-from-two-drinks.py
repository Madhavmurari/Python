class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n=len(energyDrinkA)
        dp=[[0]*2 for _ in range(n)]

        dp[0]=[energyDrinkA[0],energyDrinkB[0]]

        for i in range(1,n):
            dp[i][0]=energyDrinkA[i]+dp[i-1][0]
            dp[i][1]=energyDrinkB[i]+dp[i-1][1]

            if i-2>=0:
                dp[i][0]=max(dp[i][0],energyDrinkA[i]+dp[i-2][1])
                dp[i][1]=max(dp[i][1],energyDrinkB[i]+dp[i-2][0])

        return max(dp[n-1][0],dp[n-1][1])   