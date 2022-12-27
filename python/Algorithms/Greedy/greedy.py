class Solution:
    # 2279. Maximum Bags With Full Capacity of Rocks
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # Initialize 'lefts' list for contain the which bag can be add more rocks
        lefts = []
        # Declare 'count' for counting the full bags
        count = 0

        # first iteration is iterate through capacity list and rocks list then find which bag can add more rocks
        for i in range(len(capacity)):
            if capacity[i] - rocks[i] != 0:
                lefts.append(capacity[i] - rocks[i])
            else:
                count += 1
        # Sorting the 'lefts' list as ascending order for sort the minimum bag that can fill to full
        lefts.sort()
        # Iterate through 'lefts' list for each element subtract the additionalRocks with lefts[i] if additional rocks enough to fill bag to full and increase full back by one
        for i in range(len(lefts)):
            if additionalRocks >= lefts[i]:
                additionalRocks -= lefts[i]
                count += 1
        return count