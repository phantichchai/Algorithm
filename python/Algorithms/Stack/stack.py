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

    # 739. Daily Temperatures
    # Time complexity: O(n)
    # Space complexity: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create the 'days' stack for contain the day that not have greater temperature
        # init the first day
        days = [0]
        # create the output equal to length of temperatures
        output = [0]*len(temperatures)

        # iterate to 1 to n 
        for i in range(1, len(temperatures)):
            # loop that the the 'days' stack is not empty and ith day temperature that greater than top of the 'days' stack 
            while days and temperatures[i] > temperatures[days[-1]]:
                # update the how difference between ith day and top of the 'days' stack
                output[days[-1]] = i - days[-1]
                # pop the top of the days stack
                days.pop()
            # add ith day temperature to the 'days' stack
            days.append(i)
        return output
