class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l,r=0,k-1
        res=[]

        
        if k==1:
            return nums
        
        def consecutive(array):
            for i in range(len(array)-1):
                if array[i]+1!=array[i+1]:
                    return -1
            return 1


        while l<r and r!=len(nums):
            x=consecutive(nums[l:r+1])
            if x==-1:
                res.append(-1)
            else:
                res.append(max(nums[l:r+1]))

            l+=1
            r+=1
        return res
                

        