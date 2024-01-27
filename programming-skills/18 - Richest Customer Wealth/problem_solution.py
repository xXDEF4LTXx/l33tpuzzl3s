# You are given an m x n integer grid, accounts, where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

# Example 1:
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

# Example 2:
# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.

# Example 3:
# Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17

# Constraints:
# m == accounts.length
# n == accounts[i].length
# 1 <= m, n <= 50
# 1 <= accounts[i][j] <= 100



# This solution seems to be the best in runtime and memory - beats 99.28% of users in terms of runtime, beats 68.39% on memory
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # Create our customers list to store the sums
        customers = []
        # Iterate over the accounts and apend their sum to the customers list
        for account in accounts: customers.append(sum(account))
        # Sort the list
        customers.sort()
        # Return the last (highest) item in the list
        return customers[-1]
    
# This solution has a lower line count but only beats 27.23% of users in runtime and 61.30% in memory 
class Solution2:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # Create a customers variable that maps an anon function to sum up the accounts, converts to a list and then sort the list
        customers = list(map(lambda x: sum(x), accounts)); customers.sort()
        # Return the last (highest) item in the list
        return customers[-1]

# Tests
solution = Solution()

# Test 1
accounts = [[1,2,3],[3,2,1]]
expected = 6
output = solution.maximumWealth(accounts)
print()
assert output == expected

# Test 2
accounts = [[1,5],[7,3],[3,5]]
expected = 10
output = solution.maximumWealth(accounts)
assert output == expected

# Test 3
accounts = [[2,8,7],[7,1,3],[1,9,5]]
expected = 17
output = solution.maximumWealth(accounts)
assert output == expected

print("Passed all tests!")
