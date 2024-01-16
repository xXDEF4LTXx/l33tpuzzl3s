# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums and 1 <= len(nums) <= 10**4 and [-2**31 <= nums[nums.index(i)] <= 2**31 - 1 for i in nums]:
            for num in range(0,len(nums)):
                if nums[num] == 0: nums.pop(nums.index(nums[num])); nums.append(0)

solution = Solution()

# Test case 1: No zeroes in the list
nums = [1, 2, 3, 4, 5]
expected = [1, 2, 3, 4, 5]
solution.moveZeroes(nums)
assert nums == expected

# Test case 2: Zeroes at the beginning and end of the list
nums = [0, 1, 2, 3, 0]
expected = [1, 2, 3, 0, 0]
solution.moveZeroes(nums)
assert nums == expected

# Test case 3: Zeroes in the middle of the list
nums = [1, 0, 2, 0, 3]
expected = [1, 2, 3, 0, 0]
solution.moveZeroes(nums)
assert nums == expected

# Test case 4: All zeroes
nums = [0, 0, 0, 0, 0]
expected = [0, 0, 0, 0, 0]
solution.moveZeroes(nums)
assert nums == expected

# Test case 5: Empty list
nums = []
expected = []
solution.moveZeroes(nums)
assert nums == expected

# Test case 6: List with one element
nums = [1]
expected = [1]
solution.moveZeroes(nums)
assert nums == expected

# Test case 7: List with two elements
nums = [1, 2]
expected = [1, 2]
solution.moveZeroes(nums)
assert nums == expected

# Test case 8: List maximum length allowed in constraints
nums = [-2**31] * 10**4

expected = [-2**31] * 10**4
solution.moveZeroes(nums)
assert nums == expected

print('All tests passed successfully')