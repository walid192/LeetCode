class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)==k:
            return True

        if len(s)<k:
            return False

        cnt=collections.Counter(s)

        nbreOdd=0
        for key,value in cnt.items():
            if value%2!=0:
                nbreOdd+=1

        if nbreOdd>k:
            return False
        return True



