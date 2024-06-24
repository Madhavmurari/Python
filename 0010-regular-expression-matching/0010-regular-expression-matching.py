class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        m=len(p)
        dp={}

        def dfs(i,j):
            if i>=n and j>=m:
                return True
            if j>=m:
                return False
            if (i,j) in dp:
                return dp[(i,j)]

            match=i<n and (s[i]==p[j] or p[j]==".")
            if (j+1)<m and p[j+1]=="*":
                dp[(i,j)]=(dfs(i,j+2) or (match and dfs(i+1,j)))#Dont Use and Use '*'
                return dp[(i,j)]
            if match:
                dp[(i,j)]=dfs(i+1,j+1)
                return dp[(i,j)]
            dp[(i,j)]=False
            return False
        return dfs(0,0)
        