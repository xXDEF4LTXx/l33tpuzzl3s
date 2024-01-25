# On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

# The north direction is the positive direction of the y-axis.
# The south direction is the negative direction of the y-axis.
# The east direction is the positive direction of the x-axis.
# The west direction is the negative direction of the x-axis.
# The robot can receive one of three instructions:

# "G": go straight 1 unit.
# "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
# "R": turn 90 degrees to the right (i.e., clockwise direction).
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

# Example 1:
# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
# "G": move one step. Position: (0, 1). Direction: South.
# "G": move one step. Position: (0, 0). Direction: South.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
# Based on that, we return true.

# Example 2:
# Input: instructions = "GG"
# Output: false
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
# Based on that, we return false.

# Example 3:
# Input: instructions = "GL"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
# "G": move one step. Position: (-1, 1). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
# "G": move one step. Position: (-1, 0). Direction: South.
# "L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
# "G": move one step. Position: (0, 0). Direction: East.
# "L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
# Based on that, we return true.

# Constraints:
# 1 <= instructions.length <= 100
# instructions[i] is 'G', 'L' or, 'R'.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Check that the contraints have been met
        if 1 <= len(instructions) <= 100:
            # Set our default heading and xy coords
            heading = "North"; xy = [0,0]
            # The loop is to simulate executing the instructions multiple times - if we do not hit our start point after 4 loops a circle will not be made
            for i in range(4):
                # Iterate over the moves
                for move in instructions:
                    # Update our heading accordingly
                    if move == 'L':
                        if heading == "North": heading = "West"
                        elif heading == "East": heading = "North"
                        elif heading == "South": heading = "East"
                        elif heading == "West": heading = "South"
                    elif move == 'R':
                        if heading == "North": heading = "East"
                        elif heading == "East": heading = "South"
                        elif heading == "South": heading = "West"
                        elif heading == "West": heading = "North"
                    # Update our xy accordingly
                    elif move == 'G':
                        # Add 1 to our Y axis
                        if heading == "North": xy[1] += 1
                        # Add 1 to our X axis
                        elif heading == "East": xy[0] +=1
                        # Minus 1 from our Y axis
                        elif heading == "South": xy[1] -= 1
                        # Minus 1 from our X axis
                        elif heading == "West" : xy[0] -= 1
                # Check if we are back at our start point
                if xy == [0,0]: return True
        # Constraints not met or circle incomplete
        return False

# Tests
solution = Solution()

# Test 1
instructions = "GGLLGG"
expected = True
output = solution.isRobotBounded(instructions)
assert output == expected

# Test 2
instructions = "GG"
expected = False
output = solution.isRobotBounded(instructions)
assert output == expected

# Test 3
instructions = "GL"
expected = True
output = solution.isRobotBounded(instructions)
assert output == expected


print("Passed all tests!")
