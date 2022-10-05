from pip import List

# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(nums: List[int]) -> int:

        # Declare a variable as an int to store results of search
        
        good_pairs = 0

        """We can't just do for i in nums because we need to use the index to calculate remaining nums. Using the index function
        wouldn't work either because the list items don't have to be unique, so it would just return the first number that matches.
        Also len(nums) is used here since the last item on the list has nothing to pair it with."""

        for i in range(0, len(nums)):
            # Exclude checking indecies < i
            remaining_nums = nums[i + 1 : len(nums)]
            for j in range(0, len(remaining_nums)):
                # If the same, add one to good_pairs
                if nums[i] == remaining_nums[j]:
                    good_pairs += 1
        return good_pairs
print(Solution.numIdenticalPairs([1,2,3,1,1,3]))
print(Solution.numIdenticalPairs([1,1,1,1]))
print(Solution.numIdenticalPairs([1,2,3]))