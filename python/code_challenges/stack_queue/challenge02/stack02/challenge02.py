# Write here the code challenge solution

class Stack:
    def __init__(self):
        self.stack=[]

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_close=['()','{}','[]']
        if len(s)%2 !=0:
            return False
        
        opining= ['(','{','[']
        closing= [']','}',')']
        
        if s[0] in closing:
            return False
        
        stack=[]
        i=0
        while i<len(s):
            if s[i] in closing and len(stack)==0:
                return False
            if s[i] in opining:
                stack.append(s[i])
            else:
                if s[i] in closing and stack[-1]+s[i] in open_close:
                    stack.pop()
                else:
                    return False
            i+=1
        if len(stack) != 0:
            return False
        else:
            return True
