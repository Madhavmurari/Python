class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res=0
        prefixSum={0:1}
        summ=0

        for n in nums:
            summ+=n
            if summ-k in prefixSum:
                res+=prefixSum[summ-k]
            if summ in prefixSum:
                prefixSum[summ]+=1
            else:
                prefixSum[summ]=1
        return res
            





        