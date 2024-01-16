# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if 1 <= len(s) <= 15 and all(letter in numerals for letter in s):
            total = 0
            for i in range(len(s)):
                if i < len(s) - 1 and numerals[s[i]] < numerals[s[i+1]]: total -= numerals[s[i]]
                else: total += numerals[s[i]]
            return total


class Solution1:
    def romanToInt(self, s: str) -> int:
        numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} # Create our dict with the roman numerals and their values
        if 1 <= len(s) <= 15 and all(letter in numerals for letter in s): # Check the string meets the length requirements and all the characters in the string are roman numerals
            total = 0; skip = False; s_list = list(s) # Create our total variable, skip variable and convert the string to a list 
            for letter in s: # Iterate through the string
                    if skip: skip = False; continue # If we need to skip the current iteration, skip it and reset the skip variable to False then continue to the next iteration
                    if len(s_list) > 1 and numerals[letter] < numerals[s_list[1]]: # If the current letter's value is less than the next letter's value
                        total += (numerals[s_list[1]] - numerals[letter]); skip = True # Minus the current letter's value from the next letter's value and add it to the total, then skip the next iteration
                        for i in range(2): s_list.pop(0) # Remove the current and next letter from the list
                    else: total += numerals[letter]; s_list.pop(0) # If the current letter's value is greater than or equal to the next letter's value, add the current letter's value to the total and remove it from the list
            return total # Return the total


class Solution2:
    def romanToInt(self, s: str) -> int:
        s_list = list(s); numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if 1 <= len(s) <= 15 and all(letter in numerals for letter in s):
                total = 0; skip = False
                for letter in s:
                    if skip: skip = False; continue
                    if letter == 'I' and len(s_list) > 1:
                        if s_list[1] == 'V':
                            for i in range(2): s_list.pop(0)
                            total+=4; skip = True; continue
                        elif s_list[1] == 'X':
                            for i in range(2): s_list.pop(0)
                            total+=9; skip = True; continue
                    elif letter == 'X' and len(s_list) > 1:
                        if s_list[1] == 'L':
                            for i in range(2): s_list.pop(0)
                            total+=40; skip = True; continue
                        elif s_list[1] == 'C':
                            for i in range(2): s_list.pop(0)
                            total+=90; skip = True; continue
                    elif letter == 'C' and len(s_list) > 1:
                        if s_list[1] == 'D':
                            for i in range(2): s_list.pop(0)
                            total+=400; skip = True; continue
                        elif s_list[1] == 'M':
                            for i in range(2): s_list.pop(0)
                            total+=900; skip = True; continue
                    total += numerals[letter]; s_list.pop(0)
                return total
                    
solution = Solution()

# Test cases
# Test 1 
s = "III"
output = 3
assert solution.romanToInt(s) == output

# Test 2
s = "LVIII"
output = 58
assert solution.romanToInt(s) == output

# Test 3
s = "MCMXCIV"
output = 1994
assert solution.romanToInt(s) == output

# Test 4
s = "IX"
output = 9
assert solution.romanToInt(s) == output

# Test 5
s = "IV"
output = 4
assert solution.romanToInt(s) == output

# Test 6
s = "IIIX"
output = 11
assert solution.romanToInt(s) == output




print("All tests passed")