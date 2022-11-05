class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isWord = True
    
    def pruneWord(self, word):
        current = self
        nodeAndChildKey = []
        for char in word:
            nodeAndChildKey.append((current, char))
            current = current.children[char]

        for parentNode, childKey in reversed(nodeAndChildKey):
            targetNode = parentNode.children[childKey]
            if len(targetNode.children) == 0:
                del parentNode.children[childKey]
            else:
                return