class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        total=0
        for word in words:
            if s.startswith(word):
                total+=1
                
        return total
        