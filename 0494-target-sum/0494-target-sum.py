class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={} #(index,total)

        def bt(i,total):
            if i==len(nums):
                return 1 if total==target else 0
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)]=bt(i+1,total-nums[i])+bt(i+1,total+nums[i])
            return dp[(i,total)]

        return bt(0,0)
            