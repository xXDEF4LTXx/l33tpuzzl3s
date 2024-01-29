# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.


# Example 1:
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

# Example 2:
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false] 
# Explanation: There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

# Example 3:
# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]

# Constraints:
# n == candies.length
# 2 <= n <= 100
# 1 <= candies[i] <= 100
# 1 <= extraCandies <= 50

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Check constraints
        if 2 <= len(candies) <= 100 and 1 <= extraCandies <= 50:
            # Create a list to store the results
            candy_list = []
            # Iterate through the list of candies
            for kid in range(len(candies)):
                # Check constraints for each candy
                if 1 <= candies[kid] <= 100:
                    # Check if the kid has the greatest number of candies after adding the extra candies and append the result to the list if true
                    if (candies[kid] + extraCandies) >= max(candies): candy_list.append(True)
                    # Append false if the kid does not have the greatest number of candies after adding the extra candies
                    else: candy_list.append(False)
                # Append false if the candy does not meet the constraints
                else: candy_list.append(False)
            # Return the list of results
            return candy_list
        # Return a list of false values if the constraints are not met
        return [False for _ in range(len(candies))]

# Tests
solution = Solution()

# Test 1
candies = [2,3,5,1,3]
extraCandies = 3
expected = [True,True,True,False,True]
output = solution.kidsWithCandies(candies, extraCandies)
assert output == expected

# Test 2
candies = [4,2,1,1,2]
extraCandies = 1
expected = [True,False,False,False,False]
output = solution.kidsWithCandies(candies, extraCandies)
assert output == expected

# Test 3
candies = [12,1,12]
extraCandies = 10
expected = [True,False,True]
output = solution.kidsWithCandies(candies, extraCandies)
assert output == expected


print("Passed all tests")