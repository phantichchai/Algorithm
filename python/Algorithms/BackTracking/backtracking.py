class Solution:
    def maxLength(self, arr: list[str]) -> int:
        charSet = set()
        
        def overlap(charSet, s):
            # c = Counter(charSet) + Counter(s)
            # return max(c.values()) > 1
            prev = set()
            for c in s:
                if c in prev or c in charSet:
                    return True
                prev.add(c)
            return False
        
        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            
            result = 0
            
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                result = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(result, backtrack(i + 1))
        
        return backtrack(0)