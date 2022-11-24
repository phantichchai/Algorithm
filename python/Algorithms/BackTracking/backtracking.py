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

    # 79. Word Search
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            path.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False