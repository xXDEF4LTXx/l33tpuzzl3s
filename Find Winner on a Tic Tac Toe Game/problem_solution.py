# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

# Players take turns placing characters into empty squares ' '.
# The first player A always places 'X' characters, while the second player B always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never on filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

# Example 1:
# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# expected: "A"
# Explanation: A wins, they always play first.

# Example 2:

# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# expected: "B"
# Explanation: B wins.

# Example 3:
# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# expected: "Draw"
# Explanation: The game ends in a draw since there are no moves to make.

# Constraints:
# 1 <= moves.length <= 9
# moves[i].length == 2
# 0 <= rowi, coli <= 2
# There are no repeated elements on moves.
# moves follow the rules of tic tac toe.

class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        # Check if the constraints are met
        if 1 <= len(moves) <= 9 and all(len(i) == 2 for i in moves):
            # Create a 3x3 matrix to represent the board
            positions = [['','',''],
                        ['','',''],
                        ['','','']]
            # Create a variable to keep track of the player, and a variable to keep track of the winner
            player = 'A'; winner = ''
            # Iterate through the moves and update the board
            for move in moves:
                # If the player is A, update the board with an X, and change the player to B
                if player == 'A': val = 'X'; player = 'B'
                # If the player is B, update the board with an O, and change the player to A
                else: val = 'O'; player = 'A'
                # Update the board with the move if the position is empty
                if positions[move[0]][move[1]] == '': positions[move[0]][move[1]] = val
                # Check if there is a winner diagonally, left to right
                if positions[0][0] == positions[1][1] == positions[2][2] and positions[0][0] !='': winner = positions[0][0]
                # Check if there is a winner diagonally, right to left
                elif positions[0][2] == positions[1][1] == positions[2][0] and positions[0][2] !='': winner = positions[0][2]
                # Check if there is a winner on the top row
                elif positions[0][0] == positions[0][1] == positions[0][2] and positions[0][0] !='': winner = positions[0][0]
                # Check if there is a winner on the middle row
                elif positions[1][0] == positions[1][1] == positions[1][2] and positions[1][0] !='': winner = positions[1][0]
                # Check if there is a winner on the bottom row
                elif positions[2][0] == positions[2][1] == positions[2][2] and positions[2][0] !='': winner = positions[2][0]
                # Check if there is a winner on the left column
                elif positions[0][0] == positions[1][0] == positions[2][0] and positions[0][0] !='': winner = positions[0][0]
                # Check if there is a winner on the middle column
                elif positions[0][1] == positions[1][1] == positions[2][1] and positions[0][1] !='': winner = positions[0][1]
                # Check if there is a winner on the right column
                elif positions[0][2] == positions[1][2] == positions[2][2] and positions[0][2] !='': winner = positions[0][2]
            # Return the winner if there is one, or Pending if there are still moves to be made, or Draw if there are no more moves to be made
            if winner == 'X': return 'A'
            elif winner == 'O': return 'B'
            # Check if there are any empty positions
            if any(position == '' for position in positions[0]): return 'Pending'
            if any(position == '' for position in positions[1]): return 'Pending'
            if any(position == '' for position in positions[2]): return 'Pending'
            # If there are no empty positions, return Draw
            return 'Draw'
        # Return Pending if the constraints are not met
        return 'Pending'

# Tests
    
solution = Solution()

# Test 1
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
expected = 'A'
output = solution.tictactoe(moves)
assert solution.tictactoe(moves) == expected

# Test 2
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
expected = 'B'
assert solution.tictactoe(moves) == expected

# Test 3
moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
expected = 'Draw'
output = solution.tictactoe(moves)
assert solution.tictactoe(moves) == expected

# Test 4
moves = [[0,0],[1,1]]
expected = 'Pending'
output = solution.tictactoe(moves)
assert solution.tictactoe(moves) == expected

# Test 5
moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2]]
expected = 'Pending'
output = solution.tictactoe(moves)
assert solution.tictactoe(moves) == expected

print("Passed all tests!")