class Solution:
    def maxScore(self, s: str) -> int:

        if not s:
            return 0

        pref_zeros=0
        pref_ones=sum(1 for c in s if c=='1')
        res=-1
        for i in range(len(s)-1):
            if s[i]=='0':
                pref_zeros+=1
            else:
                pref_ones-=1
            
            res=max(res,pref_zeros+pref_ones)

        return res

