class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        l=len(s)
        current_l=0
        i=0
        while(current_l<l and i <len(words)):
            current_l+=len(words[i])
            i+=1
        
        if current_l!=l:
            return False
            
            
        result = "".join(words)
        if result.startswith(s) and len(s)>=len(words[0]):
            return True
        return False
        