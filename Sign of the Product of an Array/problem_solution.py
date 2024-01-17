
# There is a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.

# Return signFunc(product).

# Example 1:

# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1

# Example 2:

# Input: nums = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) = 0

# Example 3:

# Input: nums = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

# Constraints:

# 1 <= nums.length <= 1000
# -100 <= nums[i] <= 100
class Solution:
    def arraySign(self, nums: list[int]) -> int:
        # Check if the list meets the constraints
        if 1 <= len(nums) <= 1000 and all(-100 <= nums[i] <= 100 for i in range(len(nums))):
            # Create our product variable and set it to 1
            product = 1
            # Iterate through the list and multiply each element by the product
            for num in nums: product *= num
            # Check if the product is positive, negative, or zero and return the appropriate value
            if product >0: return 1
            elif product <0: return -1
            else: return 0

# Tests
            
solution = Solution()
# Test 1
nums = [-1,-2,-3,-4,3,2,1]
expected_output = 1
assert solution.arraySign(nums) == expected_output

# Test 2
nums = [1,5,0,2,-3]
expected_output = 0
assert solution.arraySign(nums) == expected_output

# Test 3
nums = [-1,1,-1,1,-1]
expected_output = -1

print("All tests passed.")