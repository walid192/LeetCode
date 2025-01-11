from collections import Counter
class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """

        max_counter=Counter()
        for word in words2:
            cnt=Counter(word)
            for key,value in cnt.items():
                max_counter[key]=max(max_counter[key],value)
            
        def is_universal(word):
            count = Counter(word)
            for char in max_counter:
                if count[char] < max_counter[char]:
                    return False
            return True
            
        ans=[]
        for word in words1:
            if is_universal(word):
                ans.append(word)


        return ans