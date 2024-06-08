class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        def startWith(word,pref):
            l=len(pref)
            return word[:l]==pref

        prefLength=0
        while prefLength<len(strs[0]):
            prefix=strs[0][:prefLength+1]
            for word in strs:
                if not startWith(word,prefix):
                    return strs[0][:prefLength]

            prefLength+=1

        return strs[0][:prefLength]
        