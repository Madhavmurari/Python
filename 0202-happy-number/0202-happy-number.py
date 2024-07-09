class Solution:
    def isHappy(self, n: int) -> bool:
        n_set=set()

        while n!=1:
            if n in n_set:
                return False
            n_set.add(n)
            n=sum([int(i)**2 for i in str(n)])
        
        return True