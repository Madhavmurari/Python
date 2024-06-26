class Solution:
    def numDecodings(self, s: str) -> int:
        # if s[0]=="0":
        #     return 0
        # n=len(s)
        # dp=[0]*(n+1)
        # dp[0],dp[1]=1,1

        # for i in range(2,n+1):
        #     one=int(s[i-1])
        #     two=int(s[i-2:i])

        #     if 1<=one<=9:
        #         dp[i]+=dp[i-1]
        #     if 10<=two<=26:
        #         dp[i]+=dp[i-2]
            
        # return dp[n]

        # #Memoization
        # dp={len(s):1}

        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i]=="0":
        #         return 0
            
        #     res=dfs(i+1)
        #     if i+1<len(s)and (s[i]=="1"or s[i]=="2"and s[i+1]in "0123456"):
        #         res+=dfs(i+2)
        #     dp[i]=res
        #     return res
        # return dfs(0)

        #Dynamic Progranming
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = {n: 1} #dictionary

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0  
            else:
                dp[i] = dp.get(i + 1, 0)
                if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                    dp[i] += dp.get(i + 2, 0)

        return dp[0]
            

