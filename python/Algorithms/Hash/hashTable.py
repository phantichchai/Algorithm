class Solution:
    # 290. Word Pattern
    # Time complexity: O(n)
    # Space complexity: O(n)
    def wordPattern(self, pattern: str, s: str) -> bool:
        # declare the hash map for map one to one between pattern and word
        match_p = {}
        match_word = {}
        words = s.split()
        # check if the length of word and pattern not equal then return False
        if len(pattern) != len(words):
            return False

        # iterate through both pattern and words
        for p, word, in zip(pattern, words):
            # check the word and p are not exist in hash table
            if word not in match_word and p not in match_p:
                match_word[word] = p
                match_p[p] = word
            # if the word is exist in match_word will check the pattern of that word in match_word if the p not equal in hash return False
            elif word in match_word:
                if match_word[word] != p:
                    return False
             # if the p is exist in match_p will check the word of that p in match_p if the word not equal in hash return False
            elif p in match_p:
                if match_p[p] != word:
                    return False
        # when iterate all element also the 'pattern' are match with words 's'
        return True

    # 953. Verifying an Alien Dictionary
    # M is the length of total character in words
    # N is the length of order
    # Time complexity: O(M + N)
    # Need extra space for contain the letter order 
    # Space complexity: O(1)
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # define isLexicographical for compare adjacent  word are sorted by order that given 
        def isLexicographical(first, second):
            # declare index for iterate though two word
            index = 0
            # loop though shorter length of word
            while index < min(len(first), len(second)):
                # compare the order number of i'th letter of both words
                # if the order number of letter in first are less than the order number of letter in second return True
                # if the order number of letter in first are greater than the order number of letter in second return False
                # if not above iterate to the next letter
                if order_hash[first[index]] < order_hash[second[index]]:
                    return True
                elif order_hash[first[index]] > order_hash[second[index]]:
                    return False
                else:
                    index += 1
            # if iterate all the shorter length of word then return the length of both word by length first less than equal length second
            # because if compare all letter and that not lexicographical order then we check the length between two word
            return len(first) <= len(second)
        
        # create a hash table than map the order into value for sorted alphabet order
        order_hash = { c:i for i, c in enumerate(order) }
        
        # iterate though words list
        for i in range(len(words)-1):
            # check adjacent  word are not lexicographical order then return False
            if not islexicographical(words[i], words[i+1]):
                return False
        # if iterate all word then the words are sorted by order then return True
        return True
