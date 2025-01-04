class Solution:
    def minChanges(self, s: str) -> int:
        n=len(s)

        if s=='1'*n or s=='0'*n:
            return 0

        i,j=0,1
        cnt=0
        while j<n:
            if not s[i]==s[j]:
                cnt+=1
            i+=2
            j+=2

        return cnt