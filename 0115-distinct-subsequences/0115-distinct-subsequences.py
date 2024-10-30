class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)

        # dp=[[0]*(n+1) for i in range(m+1)]

        # for i in range(m+1):
        #     dp[i][0]=1
        
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if s[i-1]==t[j-1]:
        #             dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        #         else:
        #             dp[i][j]=dp[i-1][j]
        # return dp[m][n]

#########################################################################        
        # prev=[0]*(n+1)
        # prev[0]=1
        # for i in range(1,m+1):
        #     curr=[0]*(n+1)
        #     curr[0]=1
        #     for j in range(1,n+1):
        #         if s[i-1]==t[j-1]:
        #             curr[j]=prev[j-1]+prev[j]
        #         else:
        #             curr[j]=prev[j]
        #     prev=curr[:]
        # return prev[n]

########################################################################
        prev=[0]*(n+1)
        for i in range(1,m+1):
            prev[0]=1
            for j in range(n,-1,-1):
                if s[i-1]==t[j-1]:
                    prev[j]=prev[j-1]+prev[j]
                
        return prev[n]