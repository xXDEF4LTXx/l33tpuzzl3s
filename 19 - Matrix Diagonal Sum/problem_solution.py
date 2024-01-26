# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

# Example 1:
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

# Example 2:
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8

# Example 3:
# Input: mat = [[5]]
# Output: 5

# Constraints:
# n == mat.length == mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        # Check if the there are more than 1 items
        if len(mat) > 1:
            # Create two lists to store the diagonals
            primary_diag = []; secondary_diag = []
            # Iterate over the items of mat, for as many as there are
            for i in range(len(mat)):
                # If the constraints are met, append the diagonals
                if len(mat) == len(mat[i]): primary_diag.append(mat[i][i]); secondary_diag.append(mat[i][len(mat[i])-1-i])
            # If there are an odd number of items in mat, the middle diagonals will overlap, we need to ignore one of them per the puzzle requirements, so we will pop it from the first list
            if len(mat) % 2 != 0: primary_diag.pop(int((len(mat)-1)/2))
            # Return the sum of values in both lists merged together
            return sum(primary_diag+secondary_diag)
        # Only one item inside mat, return its value
        return sum(mat[0])
# Tests
solution = Solution()

# Test 1
mat =  [[1,2,3],
        [4,5,6],
        [7,8,9]]
expected = 25
output = solution.diagonalSum(mat)
assert expected == output

mat = [[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
expected = 8
output = solution.diagonalSum(mat)
assert expected == output

mat = [[5]]
expected = 5
output = solution.diagonalSum(mat)
assert expected == output

mat = [[6,3, 1,10,7,4],
       [4,10,1,9, 5,10],
       [5,5, 7,3, 8,5],
       [2,7, 6,4, 7,6],
       [7,9, 6,1, 8,5],
       [1,7, 9,5, 8,4]]
expected = 67
output = solution.diagonalSum(mat)
assert expected == output


print("All tests passed!")

        