class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum=0
        l,r=0,len(numbers)-1
        res=[]
        while l<r:
            sum=numbers[l]+numbers[r]
            if sum>target:
                r-=1
            elif sum<target:
                l+=1
            else:
                res.append(l+1)
                res.append(r+1)
                return res
            
        return []