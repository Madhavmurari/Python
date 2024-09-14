class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        if len(height)==0:
            return []
        res=[]

        for i in range(len(height)):
            if height[i-1]>threshold:
                res.append(i)
        if 0 in res:
            res.remove(0)
        return res