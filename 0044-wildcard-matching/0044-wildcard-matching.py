class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        prev=[False]*(n+1)
        prev[0]=True

        for j in range(1,n+1):
            if p[j-1]=='*':
                prev[j]=prev[j-1]
            
        
        for i in range(1,m+1):
            curr=[False]*(n+1)
            for j in range(1,n+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    curr[j]=prev[j-1]
                elif p[j-1]=='*':
                    curr[j]=prev[j] or curr[j-1]
            prev=curr
            
        return prev[n]


        # dp=[[False]*(n+1) for i in range(m+1)]

        # dp[0][0]=True

        # for j in range(1,n+1):
        #     if p[j-1]=='*':
        #         dp[0][j]=dp[0][j-1]
            
        
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if s[i-1]==p[j-1] or s[i-1]=='?':
        #             dp[i][j]=dp[i-1][j-1]
        #         elif p[j-1]=='*':
        #             dp[i][j]=dp[i-1][j] or dp[i][j-1]
        # return dp[m][n]
        