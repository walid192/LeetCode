class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
            
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def replace(self, word):
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                return word
            node = node.children[char]
            if node.is_end_of_word:
                return word[:i + 1]
        return word

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        return ' '.join(map(trie.replace, sentence.split()))