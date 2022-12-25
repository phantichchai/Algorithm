class Solution:
    # 2389. Longest Subsequence With Limited Sum
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # define the binary search for find target and return the index from prefix sum list
        def binarySearch(target: int, nums: List[int]):
            # initlize two pointer low and high that point to first and last index of prefix list
            low = 0
            high = len(nums)-1
            # loop when low is less than high pointer
            while low < high:
                # compute mid pointer for get the value at center index
                mid = (low + high)//2
                # if target equal to value at mid index then return mid plus 1 as the accommodate 
                if target == nums[mid]:
                    return mid + 1
                # if target greater than value at mid index then move low pointer to mid plus one
                elif target > nums[mid]:
                    low = mid + 1
                # if target less than value at mid index then move high pointer to mid minus one
                else:
                    high = mid - 1
            # when finish the loop also the target value is not exist in prefix list then we can check that 
            # value at low index greater than target we return the current low value else return low index plus one
            # because the target are greater than the sumarize of each value in nums list
            return low if nums[low] > target else low + 1
        
        # initialize prefix sum list for contain sum of the value nums
        prefix = [0] * len(nums)
        # sort nums list
        nums.sort()
        # iterate through 0th to (n-1)th
        for i in range(len(nums)):
            # Add the ith prefix with preview (i-1)th prefix and add ith nums
            prefix[i] += prefix[i-1] + nums[i]
        # declare output list for contain answer
        output = []
        # iterate through each element in queries list
        for querie in queries:
            # call binary search for find the index that querie can accommodate
            output.append(binarySearch(querie, prefix))
        return output