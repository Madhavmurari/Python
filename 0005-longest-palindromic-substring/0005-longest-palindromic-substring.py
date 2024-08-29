class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s

        def expand_center(left,right):
            while left>=0 and right <len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        max_=s[0]

        for i in range(len(s)-1):
            odd=expand_center(i,i)
            even=expand_center(i,i+1)

            if len(odd)>len(max_):
                max_=odd
            if len(even)>len(max_):
                max_=even
        return max_
                    
    