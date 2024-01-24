# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

# Example 1:
# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

# Example 2:
# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
# Constraints:

# 2 <= arr.length <= 1000 - met
# -10**6 <= arr[i] <= 10**6 - met

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        # Make sure the array is within the constraints and all elements within the array are within the constraints
        if 2 <= len(arr) <= 1000 and all(-10**6 <= i <= 10**6 for i in arr):
            # If the array is only 2 elements long, return True
            if len(arr) == 2: return True
            # Sort the array and calculate the difference between the first two elements
            arr.sort(); diff = arr[1] - arr[0]
            # Iterate through the array starting at the third element and check if the difference between each element is the same, if not return False
            for i in range(2, len(arr)): 
                if arr[i] - arr[i-1] != diff: return False
            # If the loop completes without returning False, return True
            return True
        # If the array is not within the constraints, return False
        return False

# Tests

solution = Solution()

arr = [3,5,1]
expected_output = True
assert solution.canMakeArithmeticProgression(arr) == expected_output

arr = [1,2,4]
expected_output = False
assert solution.canMakeArithmeticProgression(arr) == expected_output

arr = [1,2,4,5]
expected_output = False
assert solution.canMakeArithmeticProgression(arr) == expected_output

arr = [1,2,4,5,6]
expected_output = False
assert solution.canMakeArithmeticProgression(arr) == expected_output

arr = [1] * 1000
expected_output = True
assert solution.canMakeArithmeticProgression(arr) == expected_output

arr = [1,10,10,10,19]
expected_output = False
assert solution.canMakeArithmeticProgression(arr) == expected_output

print("All tests passed")