class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ''
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)  # Handle multi-digit numbers
            elif char == '[':
                stack.append((current_string, current_num))
                current_string, current_num = '', 0  # Reset for new string and num
            elif char == ']':
                last_string, num = stack.pop()
                current_string = last_string + current_string * num  # Decode
            else:
                current_string += char  # Build current string
        
        return current_string




        