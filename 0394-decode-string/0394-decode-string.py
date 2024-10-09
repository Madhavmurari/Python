class Solution:
    def decodeString(self, s: str) -> str:

        stack=[]
        for char in s:
            if char!=']':
                stack.append(char)
            else:
                temp1=''
                while stack[-1]!='[':
                    temp1=stack.pop() + temp1
                stack.pop()

                temp2=''
                while stack and stack[-1].isdigit():
                    temp2=stack.pop()+temp2
                temp1=int(temp2)*temp1
                stack.append(temp1)
            
        return ''.join(stack)



        