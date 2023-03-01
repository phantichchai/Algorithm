class Solution:
    # 912. Sort an Array
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def sortArray(self, nums: List[int]) -> List[int]:
        # Conquer step
        def conquer(L, M, R):
            # Create the first and second half from original array
            left, right = nums[L:M+1], nums[M+1:R+1]
            # initilize i, j, k pointer for iterate thought entrire array by current sort element, first element of left, first element of right respectively
            i, j, k = L, 0, 0

            # iterate untiil which pointer iterate all the own half array
            while j < len(left) and k < len(right):
                # if the left at index j less than equal to the right at index k then set the value in original array at index i equal to left at index j and move pointer j to next element
                # else in contrast set set the value in original array at index i equal to right at index k and move pointer k to next element
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                # move current sort to next element
                i += 1
            # iterate through the left element and set than to original array
            while j < len(left):
                nums[i] = left[j]
                i += 1
                j += 1
            # iterate through the right element and set than to original array
            while k < len(right):
                nums[i] = right[k]
                i += 1
                k += 1

        # Divide step
        def divide(l, r):
            # Base case for check when the l pointer and r pointer are the same mean the value are the one value before conquer step
            if l == r:
                return nums
            # find mid value for divide array into two half
            m = (l + r) // 2
            # divide first half stack untill base case
            divide(l, m)
            # divide second half stack until base case
            divide(m+1, r)
            # call conquer step
            conquer(l, m, r)
            # return the nums that sorted array
            return nums

        return divide(0, len(nums)-1)