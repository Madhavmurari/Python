from collections import defaultdict
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n=len(word)
        vow="aeiou"
        count=0

        for left in range(n):
            f=collections.Counter()
            cons_count=0

            for right in range(left,n):
                if word[right] in vow:
                    f[word[right]]+=1
                else:
                    cons_count+=1
                
                if cons_count>k:
                    break
                if cons_count==k and all(f[v]>=1 for v in vow):
                    count+=1
        return count


            
            
        