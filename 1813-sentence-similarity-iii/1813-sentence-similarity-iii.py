class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()

        if len(s1) > len(s2):
            s1, s2 = s2, s1

        i, j = 0, 0
        while i < len(s1) and s1[i] == s2[i]:
            i += 1
        while j < len(s1) - i and s1[len(s1) - 1 - j] == s2[len(s2) - 1 - j]:
            j += 1

        return i + j == len(s1)