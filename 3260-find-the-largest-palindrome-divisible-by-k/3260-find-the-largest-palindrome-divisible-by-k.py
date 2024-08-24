# class Solution:
#     def is_palindrome(self, x: str) -> bool:
#         return x == x[::-1]

#     def largestPalindrome(self, n: int, k: int) -> str:
#         # Largest n-digit number
#         max_n_digit = 10**n - 1

#         # Iterate from max_n_digit downwards
#         for i in range(max_n_digit, 0, -1):
#             if i % k == 0 and self.is_palindrome(str(i)):
#                 return str(i)
        
#         # If no such number exists (though per constraints there should be), return empty string
#         return ""

class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:

        if k==1 or k==3 or k==9:
            return '9'*n

        if k==2:
            if n==1:return '8'
            if n==2:return '88'
            if n>2:return '8'+'9'*(n-2)+'8'
        
        if k==4:
            if n<=4:return '8'*n
            if n>4: return '88'+'9'*(n-4)+'88'

        if k==5:
            if n==1:return '5'
            if n==2:return '55'
            if n>2:return '5'+'9'*(n-2)+'5'
        
        if k==6:
            if n <= 2:
                return "6" * n
            if n == 3:
                return "888"
            if n % 2 == 1:
                return "8" + ((n - 3)//2)*"9" + "8" + ((n - 3)//2)*"9" + "8"
            if n % 2 == 0:
                return "8" + ((n - 3) // 2) * "9" + "77" + ((n - 3) // 2) * "9" + "8"
        if k==7:
            dic = {0: '', 1: '7', 2: '77', 3: '959', 4: '9779', 5: '99799', 6: '999999', 7: '9994999',
                       8: '99944999', 9: '999969999', 10: '9999449999', 11: '99999499999'}
            l, r = divmod(n, 12)
            return '999999' * l + dic[r] + '999999' * l
        if k==8:
            if n<=6:return '8'*n
            if n>6:return '888'+'9'*(n-6)+'888'
        else:
            return ""
            



