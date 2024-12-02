class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        res=""
        for word in words:
            res+=word
            if(res==s):
                return True
            if(not s.startswith(res)):
                return False
        
        return False
        