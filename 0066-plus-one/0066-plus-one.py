class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        for i in range(len(digits)):
            result = result * 10 + digits[i]

        result = result + 1
        return [int(x) for x in str(result)]
