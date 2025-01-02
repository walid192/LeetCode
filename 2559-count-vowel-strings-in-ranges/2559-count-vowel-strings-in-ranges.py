class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels={'a','e','i','u','o'}
        cnt=[]
        for word in words:
            if word[0] in vowels and word[-1]in vowels:
                if len(cnt):
                    cnt.append(1+cnt[-1])
                else:
                    cnt.append(1)
            else:
                if len(cnt):
                    cnt.append(cnt[-1])
                else:
                    cnt.append(0)
                
        cnt=[0]+cnt
        ans=[]
        for l,r in queries:
            ans.append(cnt[r+1]-cnt[l])

        return ans
        