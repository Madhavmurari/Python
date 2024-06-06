class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res=nums[0]
        curMax,curMin=1,1

        for n in nums:

            temp=n*curMax
            curMax=max(n*curMax,n*curMin,n)
            curMin=min(temp,n*curMin,n)
            res=max(res,curMax)
        return res