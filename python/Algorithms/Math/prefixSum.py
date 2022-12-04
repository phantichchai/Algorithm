class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # declare variables that for use before computational
        # n is a length of th nums
        # sum1 and sum2 is the temperal sum of term i+1 and term n-i-1
        # MAD is higher posible value for a minimum average difference in this problem
        # res storing for the index that has minimum average difference
        n = len(nums)
        sum1, sum2 = 0, sum(nums)
        MAD = pow(10,5)
        res = 0
        
        # this loop for iterate though index 'i' to index 'n-1' 
        for i in range(n):
            # add the num of index 'i' to sum1 for compute first term of MAD
            # subtact the num of index 'i' to sum2 for compute secound term of MAD
            sum1 += nums[i]
            sum2 -= nums[i]
            
            # check if i is a last element of average diffence then it has equal to first term because avoid diviend by zero
            # else compute by find absolute value difference between floor the first term diviend by i + 1 
            # and floor the second term diviend by n-i-1 
            if i == n-1:
                avg_diff = abs(floor(sum1/n))
            else:
                avg_diff = abs(floor(sum1/(i+1)) - floor(sum2/(n-i-1)))
            
            # compare averate difference is less than current minimum averate difference then assign new minimum averate difference
            # and the index of minimum averate difference
            if avg_diff < MAD:
                MAD = avg_diff
                res = i
        # return the index of minimum averate difference
        return res