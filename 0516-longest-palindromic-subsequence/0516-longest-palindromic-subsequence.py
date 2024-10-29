class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # def isPalindrome(s):
        #     left,right=0,len(s)-1

        #     while left < right:
        #         if s[left]!=s[right]:
        #             return False
        #         else:
        #             left+=1
        #             right-=1
        #     return True
        
        # res=[]
        # subset=[]

        # def subsequence(i,s):
        #     if i ==len(s):
        #         if isPalindrome(''.join(subset.copy())):
        #             res.append(''.join(subset.copy()))
        #         return
            
        #     subset.append(s[i])
        #     subsequence(i+1,s)
        #     subset.pop()
        #     subsequence(i+1,s)
        # subsequence(0,s)

        # max_length=0
        # for st in res:
        #     max_length=max(max_length,len(st))

        # return max_length
######################################################################
        # n=len(s)
        # t=s[::-1]  #t=''.join(reversed(s))
        # dp=[[0]*(n+1) for i in range(n+1)]
        # ans=0
        # for i in range(1,n+1):
        #     for j in range(1,n+1):
        #         if s[i-1]==t[j-1]:
        #             dp[i][j]=1+dp[i-1][j-1]
        #         else:
        #             dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        # return dp[n][n]

###########################################################################
        n=len(s)
        t=s[::-1]

        prev=[0]*(n+1)
        for i in range(1,n+1):
            curr=[0]*(n+1)
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(curr[j-1],prev[j])
            prev=curr[:]
        return prev[n]
