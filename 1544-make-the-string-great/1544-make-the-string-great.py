class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        
        for i in range(len(s)):
            if(stack and abs(ord(stack[-1])-ord(s[i]))==32):
                stack.pop()
            else:
                stack.append(s[i])
            
        return ''.join(stack)
            
        