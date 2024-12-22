class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        pattern_to_s={}
        s_to_pattern={}
        
        
        s=s.split()
        
        if len(s)!=len(pattern):
            return False
        
        for i,word in enumerate(s):
            if word in s_to_pattern:
                if s_to_pattern[word]!=pattern[i]:
                    return False
            else:
                s_to_pattern[word]=pattern[i]
                
            
            if pattern[i] in pattern_to_s:
                if pattern_to_s[pattern[i]]!=word:
                    return False
            else:
                pattern_to_s[pattern[i]]=word
                
        return True
                
            
                
        