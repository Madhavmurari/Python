class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # def f(ind, prev_ind):
        #     if ind == n:
        #         return 0
        #     # Option 1: Exclude current element
        #     length = f(ind + 1, prev_ind)
            
        #     if prev_ind == -1 or nums[ind] > nums[prev_ind]:
        #         length = max(length, 1 + f(ind + 1,ind))
            
        #     return length
        # return f(0, -1)
###########################################################################
        # dp={}
        # def f(ind, prev_ind):
        #     if ind == n:
        #         return 0
        #     if(ind,prev_ind) in dp:
        #         return dp[(ind,prev_ind)]
        #     # Option 1: Exclude current element
        #     length = f(ind + 1, prev_ind)
            
        #     if prev_ind == -1 or nums[ind] > nums[prev_ind]:
        #         length = max(length, 1 + f(ind + 1,ind))
            
        #     dp[(ind,prev_ind)]=length
        #     return length
        # return f(0, -1)
###########################################################################
        if n==0:
            return 0
        dp=[1]*n

        for i in range(1,n):
            for j in range(0,i):

                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)


          


        
        