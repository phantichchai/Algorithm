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
