class Solution:
    # 35. Search Insert Position
    # Time complexity: O(log(N))
    # Space complexiy: O(1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        # declare pointer low and high for point to the first index and las index respectively
        low, high = 0, len(nums)-1
        # check that target greater than the last index of nums so the index of target is the last of array nums
        if target > nums[-1]:
            return high + 1

        # while loop still low is less than high
        while low <= high:
            # declare the mid index of two pointer high and low for check the value of mid index by high plus low divide by 2
            mid = (high + low) // 2
            # check if the value of mid index equal to target then the mid index should be the target index
            if nums[mid] == target:
                return mid
            # move high pointer to mid index minus 1 if the value of mid index greater than target in contrast move low pointer to
            # mid index plus 1 
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        # if the pointer index is greater than high also the target index should be low pointer index
        return low