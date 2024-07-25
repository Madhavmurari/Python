class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a,b,c=0,0,0

        for i in range(len(triplets)):
            if triplets[i][0]<=target[0] and triplets[i][1]<=target[1] and triplets[i][2]<=target[2]:
                a=max(a,triplets[i][0])
                b=max(b,triplets[i][1])
                c=max(c,triplets[i][2])
            if a==target[0] and b==target[1] and c==target[2]:
                return True
        return False