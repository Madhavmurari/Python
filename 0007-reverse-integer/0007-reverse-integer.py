class Solution:
    def reverse(self, x: int) -> int:
        Max=2147483647
        Min=-2147483648
        res=0

        while x:
            rem=int(math.fmod(x,10))   #python is dump -1 % 10 = 9
            
            if (res>Max//10) or (res==Max//10 and rem>=Max%10 ):
                return 0
            if (res<Min//10) or (res==Min//10 and rem<=Min%10):
                return 0
            res=res*10+rem
            x=int(x/10)     #-1//10=-1
        return res