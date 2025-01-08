class Solution:

    def isPrefixAndSuffix(self,str1,str2):
        if len(str1)>len(str2):
            return False

        if str2.startswith(str1) and (str2[::-1].startswith(str1[::-1])):
            return True

        return False

 


    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt=0
        for i,word in enumerate(words):
            for j in range(i+1,len(words)):
                if self.isPrefixAndSuffix(word, words[j]):
                    cnt+=1

        return cnt

 
        