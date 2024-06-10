class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s=="":
            return True
        
        stack=[]
        mapping={
            "(":")",
            "{":"}",
            "[":"]",
            "":""
        }
        
        if s[0] not in mapping:
            return False
        
        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if stack==[]:
                    return False
                todel=stack[len(stack)-1]
                if mapping[todel]==char:
                    stack.pop()
                else:
                    return False
                
        return len(stack)==0
                
        