# There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

# You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

# Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

# Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.


# Example 1:
# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

# Example 2:
# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

# Constraints:
# 1 <= moves.length <= 2 * 10**4
# moves only contains the characters 'U', 'D', 'L' and 'R'.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Check constraints are met
        if 1 <= len(moves) <= 2 * 10**4:
            # Set our original position
            xy = [0,0]
            for move in moves:
                # Increase our Y value if we are going up
                if move == 'U': xy[1] += 1 
                # Decrease our Y value if we are going down
                elif move == 'D': xy[1] -= 1 
                # Increase our X value if we are going right
                elif move == 'R': xy[0] += 1 
                # Decrease our X value if we are going left
                elif move == 'L': xy[0] -= 1 
            # Check if we are back to the original position
            if xy == [0,0]: return True
        # Return False (constraints not met or we are not at the original position)
        return False 

# Tests
solution = Solution()

moves = "UD"
output = True
assert solution.judgeCircle(moves) == output

moves = "LL"
output = False
assert solution.judgeCircle(moves) == output

