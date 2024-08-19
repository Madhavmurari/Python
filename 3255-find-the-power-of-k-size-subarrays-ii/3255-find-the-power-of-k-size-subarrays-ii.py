from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[]
        streak=0

        for i in range(n):
            if i==0 or nums[i]==nums[i-1]+1:
                streak+=1
            else:
                streak=1
            
            if i+1>=k:
                if streak>=k:
                    res.append(nums[i])
                else:
                    res.append(-1)
        return res
