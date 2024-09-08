class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:

        # n=len(nums)
        # if n==1 or n==0:
        #     return 0
        # dp=[0]*(n)
        # dp[n-1]=0
        # for i in range(n-2,-1,-1):
        #     for j in range(i+1,n):
        #         dp[i]=max((j-i)*nums[i]+dp[j],dp[i])
        # return dp[0]

        ans = 0
        cmax = 0
        for x in nums[:-1]:
            cmax = max(cmax, x)
            ans += cmax
        return ans
        
      
        