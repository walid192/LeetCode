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

    def longest_common_prefix(self):
        node = self.root
        prefix = []
        while node and len(node.children) == 1 and not node.is_end_of_word:
            char, next_node = next(iter(node.children.items()))
            prefix.append(char)
            node = next_node
        return ''.join(prefix)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""

        trie = Trie()
        for word in strs:
            trie.insert(word)

        return trie.longest_common_prefix()
        