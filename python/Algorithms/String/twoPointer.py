class Solution:
    # 28. Find the Index of the first Occurrence in a String
    # Time complexity: O(n + m) by n is the length of haystack and m is the length of needle
    # Space complexity: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        # compare length of needle and haystack that length of needle greater than haystack that can solve that
        # the needle can't be part of haystack.
        if len(needle) > len(haystack):
            return -1
        # iterate thought length of haystack subtract with needle for compare every substring of haystack
        for i in range(len(haystack)-len(needle)+1):
            # initial j pointer for iterate the substring in needle
            j = 0
            # declare variable for check than needle is a part of haystack
            match = False
            # iterate compare every of character of haystack and needle that can match
            while j < len(needle):
                # compare and move the j pointer to next character
                if haystack[i+j] == needle[j]:
                    j += 1
                    # set match equal to true if the both chacter are match
                    match = True
                else:
                    # set match equal to true if the both chacter aren't match and break loop
                    match = False
                    break
            # return index i if needle is a part of haystack
            if match:
                return i
        # if iterate all possible substring of haystack and not found index then the needle isn't part of haystack
        return -1