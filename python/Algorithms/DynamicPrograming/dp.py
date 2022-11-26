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

if __name__ == "__main__":
    solution = Solution()
    print(solution.jobScheduling([1,2,3,3], [3,4,5,6],[50,10,40,70]))
    