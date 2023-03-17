# Create TrieNode structure
class TrieNode:
    def __init__(self):
        # each node will contain all possible character in which level of tree and boolean endOfword for check that is the end of word
        self.children = {}
        self.endOfWord = False

class Trie:
    # initialize root trie node
    def __init__(self):
        self.root = TrieNode()

    # Time Complexity O(n): n is the length of word
    # Space Complexity O(1)
    # insert trie node
    def insert(self, word: str) -> None:
        # set the current node for iterate through trie node
        cur = self.root
        # iterate each character in word
        for c in word:
            # check that c not in trie then crete new children trie node for that character
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # move to the next trie node
            cur = cur.children[c]
        # when iterate all word set the last character of this word to True
        cur.endOfWord = True

    # Time Complexity O(n): n is the length of word
    # Space Complexity O(1)
    # search trie node
    def search(self, word: str) -> bool:
        # set the current node for iterate through trie node
        cur = self.root
        # iterate each character in word
        for c in word:
            # check that c not in trie then return False because this word not in trie
            if c not in cur.children:
                return False
            # move to the next trie node
            cur = cur.children[c]
        # when iterate all word that show the word has in trie then return the endOfword
        return cur.endOfWord
        
    # Time Complexity O(n): n is the length of prix
    # Space Complexity O(1)
    # startWith trie node
    # same as search but return true when iterate all prefix and false when the character's not in trie
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True