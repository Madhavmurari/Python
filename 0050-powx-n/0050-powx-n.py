class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==0:
            return 1
        if n<0:
            x**=-1  #x=1/x
            n*=-1   #n=-n
        if n%2==1:
            return x*self.myPow(x,n-1)
        else:
            num=self.myPow(x,n//2)
            return num*num