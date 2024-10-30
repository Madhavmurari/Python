class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        m,n=len(str1),len(str2)
        dp=[[0]*(n+1) for i in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        lcs=[]
        while m>0 and n>0:
            if str1[m-1]==str2[n-1]:
                lcs.append(str1[m-1])
                m-=1
                n-=1
            elif dp[m-1][n]>dp[m][n-1]:
                lcs.append(str1[m-1])
                m-=1
            else:
                lcs.append(str2[n-1])
                n-=1
        while m>0:
            lcs.append(str1[m-1])
            m-=1
        while n>0:
            lcs.append(str2[n-1])
            n-=1

        return ''.join(reversed(lcs))
        

