# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Check if the length of the list == 1 and if the element is a zero, if so, return [1]
        if len(digits) == 1 and digits[0] == 0: return [1]
        # Check if the list fits the constraints and if the first element isn't a zero
        elif 1 <= len(digits) <= 100 and all(0 <= digits[i] <= 9 for i in range(len(digits))) and digits[:1][0] != 0:
            # Convert the list to an integer, add 1, convert back to a list, and return it
            n = int(''.join(str(digit) for digit in digits)); n+=1
            # Return the list of digits
            return list([int(x) for x in list(str(n))])
        
# Tests

solution = Solution()

# Test case 1: Single-digit number
digits = [5]
expected_output = [6]
try: assert solution.plusOne(digits) == expected_output
except AssertionError: print(f"Test case 1 failed: {solution.plusOne(digits)} != {expected_output}")
# Test case 2: Number with multiple digits
digits = [1, 2, 3]
expected_output = [1, 2, 4]
assert solution.plusOne(digits) == expected_output

# Test case 3: Number with trailing zeros
digits = [1, 2, 3, 0, 0]
expected_output = [1, 2, 3, 0, 1]
assert solution.plusOne(digits) == expected_output

# Test case 4: Number with all nines
digits = [9, 9, 9]
expected_output = [1, 0, 0, 0]
assert solution.plusOne(digits) == expected_output

# Test case 5: Number with leading zero
digits = [0, 1, 2, 3]
expected_output = None
assert solution.plusOne(digits) == expected_output

# Test case 6: 100 9s
digits = [9] * 100
expected_output = [1] + [0] * 100
assert solution.plusOne(digits) == expected_output

# Test case 7: Empty list
digits = []
expected_output = None
assert solution.plusOne(digits) == expected_output

# Test case 8: List with just a zero
digits = [0]
expected_output = [1]
assert solution.plusOne(digits) == expected_output

print("All test cases passed!")