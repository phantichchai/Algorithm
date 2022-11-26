class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in list(s):
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

    # 907. Sum of Subarray Minimums
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        MOD = 10**9 + 7
        sum_of_minimums = 0
        
        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i
                count = (mid - left_boundary) * (right_boundary - mid)
                sum_of_minimums += count * arr[mid]
            stack.append(i)
            
        return sum_of_minimums % MOD