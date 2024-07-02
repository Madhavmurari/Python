class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:].zfill(32)
        # Reverse the binary string
        reversed_str = binary_str[::-1]
        # Convert the reversed binary string back to an integer
        return int(reversed_str, 2)

        res=0
        for i in range(32):
            bit =(n>>i)&1
            res+=(bit<<(31-i))
        return res