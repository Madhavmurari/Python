class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        ans = 1
        i = 0
        while i < n:
            ch = word[i]
            cnt = 0
            while i < n and word[i] == ch:
                i += 1
                cnt += 1
            ans  += cnt - 1
        return ans
        
        