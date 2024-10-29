class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        t=s[::-1]
        
        # dp=[[0]*(n+1) for i in range(n+1)]
        # for i in range(1,n+1):
        #     for j in range(1,n+1):
        #         if s[i-1]==t[j-1]:
        #             dp[i][j]=1+dp[i-1][j-1]
        #         else:
        #             dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        # return n-dp[n][n]
        

        prev=[0]*(n+1)
        for i in range(1,n+1):
            curr=[0]*(n+1)
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(prev[j],curr[j-1])
            prev=curr[:]
        return n-prev[n]
        