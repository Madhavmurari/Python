class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum=sum(nums)
        dp=set()
        dp.add(0)
        n=len(nums)

        if Sum%2:
            return False
        target=Sum//2
        
        for i in range(n-1,-1,-1):
            nextdp=set()
            for j in dp:
                if (j+nums[i])==target:
                    return True
                nextdp.add(j+nums[i])
                nextdp.add(j)
            dp=nextdp
        return True if target in dp else False