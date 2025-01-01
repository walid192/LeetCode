class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root=Node()
        

    def addWord(self, word: str) -> None:
        current=self.root
        for c in word:
            if c not in current.children:
                current.children[c]=Node()

            current=current.children[c]
        current.is_word=True
            

    def search(self, word: str) -> bool:
        def dfs(node,i):

            if i==len(word):
                return node.is_word
            
            c=word[i]

            if c=='.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if c in node.children:
                    return dfs(node.children[c], i + 1)
                else:
                    return False
            
        return dfs(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)