from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransome_cnt=Counter(ransomNote)
        magazine_cnt=Counter(magazine)
        
        for key,value in ransome_cnt.items():
            if not magazine_cnt[key] or not magazine_cnt[key]>=value:
                return False
            
        return True
        