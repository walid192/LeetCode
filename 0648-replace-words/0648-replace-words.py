class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        def subWord(s,word):
            if(len(s)>len(word)):
                return False
            for i in range(len(s)):
                if(s[i]==word[i]):
                    pass
                else:
                    return False

            return True

        wordsToChange=[]

        words=sentence.split(' ')
        for i in range(len(words)):
            for root in dictionary:
                if(subWord(root,words[i])):
                    words[i]=root


        return ' '.join(words)