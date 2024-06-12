class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        res=0
        chars=[]
        
        for r in range(len(s)):
            while(s[r]in chars):
                chars.remove(s[l])
                l+=1
            
            chars.append(s[r])
            res=max(res,r-l+1)
            
        return res
                
            
            
        