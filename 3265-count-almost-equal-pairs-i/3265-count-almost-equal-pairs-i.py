class Solution:
    def countPairs(self, nums: List[int]) -> int:
        N=len(nums)
        res=0
        for i in range(N-1):
            for j in range(i+1,N):
                n1=str(nums[i])
                n2=str(nums[j])

                if len(n1)>len(n2):
                    n2='0'*(len(n1)-len(n2))+n2
                if len(n2)>len(n1):
                    n1='0'*(len(n2)-len(n1))+n1

                count=0
                for k in range(len(n2)):
                    if n1[k]!=n2[k]:
                        count+=1
                if count<=2 and sorted(n1)==sorted(n2):
                    res+=1
        return res
        