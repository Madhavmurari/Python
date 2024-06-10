class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n-=1
        round = k // n
        rem = k % n

        if round % 2 == 0:
            return rem
        else:
            return n-rem
