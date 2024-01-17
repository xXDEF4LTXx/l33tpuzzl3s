# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Example 1:

# Input: nums = [1,2,2,3]
# Output: true

# Example 2:
# Input: nums = [6,5,4,4]
# Output: true

# Example 3:
# Input: nums = [1,3,2]
# Output: false

# Constraints:

# 1 <= nums.length <= 10**5 - met
# -10**5 <= nums[i] <= 10**5 - met

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        # Make sure the list is within the constraints
        if 1 <= len(nums) <= 10**5 and all(-10**5 <= i <= 10**5 for i in nums):
            # Create an index and a list to store whether the numbers are positive, negative, or equal to each other
            index = 0; found = []
            # Loop through the list of numbers
            for i in range(len(nums)):
                # If the index is less than the length of the list minus 1, check if the number at the current index is greater than, less than, or equal to the number at the next index
                if i < len(nums)-1:
                    # If the number at the current index is greater than the number at the next index, add 'pos' to the list
                    if nums[i] > nums[i+1]: found.append('pos')
                    # If the number at the current index is less than the number at the next index, add 'neg' to the list
                    elif nums[i] < nums[i+1]: found.append('neg')
                    # If the number at the current index is equal to the number at the next index, add 'equ' to the list
                    else: found.append('equ')
                # Remove duplicates from the list
                found = list(dict.fromkeys(found))
                # If both 'pos' and 'neg' are in the list, return False
                if 'pos' in found and 'neg' in found: return False
            # If the list only contains 'pos' and 'equ' or 'neg' and 'equ', return True
            return True
        # If the list is not within the constraints, return False
        return False
    
# Tests
    
solution = Solution()

# Test case 1: Monotone increasing with duplicates alongside each other
nums = [1,2,2,3]
assert solution.isMonotonic(nums) == True

# Test case 2: Monotone decreasing with duplicates alongside each other
nums = [6,5,4,4]
assert solution.isMonotonic(nums) == True

# Test case 3: Not monotone
nums = [1,3,2]
assert solution.isMonotonic(nums) == False

# Test case 4
nums = [1,1,0]
assert solution.isMonotonic(nums) == True

# Test case 5
nums = [1,1,1]
assert solution.isMonotonic(nums) == True

# # Test case 6
nums = [2,2,2,1,4,5]
assert solution.isMonotonic(nums) == False

