# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

# Example 1:
# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

# Example 2:
# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

# Example 3:
# Input: ops = ["1","C"]
# Output: 0
# Explanation:
# "1" - Add 1 to the record, record is now [1].
# "C" - Invalidate and remove the previous score, record is now [].
# Since the record is empty, the total sum is 0.
 
# Constraints:
# 1 <= operations.length <= 1000
# operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10**4, 3 * 10**4].
# For operation "+", there will always be at least two previous scores on the record.
# For operations "C" and "D", there will always be at least one previous score on the record.
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        # Make sure our operations list meets the constraints
        if 1 <= len(operations) <= 1000 and all(-3 * 10**4 <= int(op) <= 3 * 10**4 for op in operations if (op.isdigit() or '-' in op)):
            # Create scores list
            scores = []
            # Iterate over the list
            for op in operations:
                # Check if isdigit or see if '-' is in it, append if so and continue 
                if op.isdigit() or '-' in op:
                        # Check if the int fits the constraints
                        if (-3 * 10**4 <= int(op) <= 3 * 10**4): scores.append(int(op)); continue
                # If the op is +, append the sum of value of the last two list items
                elif op == '+': scores.append(scores[-1]+scores[-2]); continue
                # If the op is D, append the last item * 2
                elif op == 'D': scores.append(scores[-1]*2); continue
                # If the op is C, remove the last list item
                elif op == 'C': scores.pop(); continue
            # Return the sum of all scores
            return sum(scores)

# Tests
solution = Solution()

ops = ["5","2","C","D","+"]
output  = 30
assert solution.calPoints(ops) == output

ops = ["5","-2","4","C","D","9","+","+"]
output = 27
assert solution.calPoints(ops) == output

ops = ["1","C"]
output = 0
assert solution.calPoints(ops) == output

ops = ["1","C","-30001"]
output = None
assert solution.calPoints(ops) == output

ops = ["1","C","30001"]
output = None
assert solution.calPoints(ops) == output

print("All tests passed")