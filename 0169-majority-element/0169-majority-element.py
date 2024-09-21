class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # n=len(nums)
        # return nums[n//2]

        # mapp={}
        # for n in nums:
        #     mapp[n]=1+mapp.get(n,0)
        
        # return max(mapp, key=mapp.get) 
        
        count=0
        candidate=0

        for n in nums:
            if count==0:
                candidate=n
            if n==candidate:
                count+=1
            else:
                count-=1
        return candidate
