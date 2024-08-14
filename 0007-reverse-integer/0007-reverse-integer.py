class Solution:
    def reverse(self, x: int) -> int:
        Max=(2**31)-1
        Min=-(2**31)
        res=0

        while x:
            rem=int(math.fmod(x,10))  # (python dump)-1 % 10 = 9
            if (res>Max // 10) or (res==Max//10 and rem > Max%10):
                return 0
            if (res<Min//10) or (res==Min//10 and rem < Min%10):
                return 0
            x=int(x/10)   # -1//10 = -1
            res=res*10+rem
        return res