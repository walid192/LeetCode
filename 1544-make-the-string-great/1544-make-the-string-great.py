class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=="":
            return s
        i = 0
        while i < len(s) - 1:
            if s[i] != s[i+1] and (s[i].lower() == s[i+1] or s[i].upper() == s[i+1]):
                s = s[:i] + s[i+2:]
                return self.makeGood(s)  
            else:
                i += 1
        
        return s
            
        