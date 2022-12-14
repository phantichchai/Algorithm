import bisect
from typing import List

class Solution:
    # 1235. Maximum Profit in Job Scheduling
    # Bisection method
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [[0, 0]]
        def f(x):
            return dp[bisect.bisect_left(dp, [x+1])-1][1]
        for e, s, p in sorted(zip(endTime, startTime, profit)):
            dp.append([e, max(f(e), f(s)+p)])
        return dp[-1][1]

    # TLE
    def TLE(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))
        
        def rec(i):
            if i == N:
                return 0
            j = i + 1
            while j < N and jobs[i][1] > jobs[j][0]:
                j += 1
            return max(jobs[i][2] + rec(j), rec(i+1))    
        
        return rec(0)

    # 70. Climbing Stairs
    def climbStairs(self, n: int) -> int:
        # one mean the possible distinct ways when climp one step from current stair
        # two mean the possible distinct ways when climp two step from current stair
        one, two = 1, 1
        for _ in range(n):
            one, two = one + two, one
        return one

    # 198. House Robber
    def rob(self, nums: List[int]) -> int:
        # declare the 'rob1' and 'rob2' for contain a amount of money than you can get in each plan with 0
        rob1, rob2 = 0, 0

        # iterate thourgh in the list 'nums' 
        for num in nums:
            # find maximum between the amount of money that you rob1 path with the current house and rob2 path
            temp = max(rob1+num, rob2)
            # store the rob2 path in rob1 path mean the previous maximum the amount of money you can get in this path
            rob1 = rob2
            # store the new maximum path to the rob2
            rob2 = temp
        return rob2

if __name__ == "__main__":
    solution = Solution()
    print(solution.jobScheduling([1,2,3,3], [3,4,5,6],[50,10,40,70]))
    