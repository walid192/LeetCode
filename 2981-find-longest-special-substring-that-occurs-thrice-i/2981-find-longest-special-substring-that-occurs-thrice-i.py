from collections import defaultdict

class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        subs=defaultdict(int)
        
        i=0
        
        while(i<len(s)):
            subs[s[i]]+=1
            j=i+1

            while(j<len(s) and s[i]==s[j]):
                subs[s[i:j+1]]+=1
                j+=1
 
            i+=1
        sorted_values=sorted(subs.items(), key=lambda x: len(x[0]), reverse=True)
        res=[key for key,value in sorted_values if value>=3 ] 
        if not res:
            return -1
        
        return len(res[0])        
        
        
        
                
