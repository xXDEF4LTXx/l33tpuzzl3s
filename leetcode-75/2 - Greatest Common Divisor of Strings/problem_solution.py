# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if the input strings are valid length and characters
        if 1 <= len(str1) <= 1000 and 1 <= len(str2) <= 1000 and all(letter in 'abcdefghijklmnopqrstuvwxyz' for letter in (str1+str2).lower()):
            # Create two lists of strings that are divisors of the input strings
            str1_strings = []; str2_strings = []
            # Loop through the length of the longest string and append the divisors to the lists
            for divisor in range(1, len(str1)+1 if len(str1) > len(str2) else len(str2)+1):
                # Check if the divisor is valid for the string and append it to the list
                if len(str1) % divisor == 0: str1_strings.append(str1[:int(len(str1)/divisor)])
                if len(str2) % divisor == 0: str2_strings.append(str2[:int(len(str2)/divisor)])
            # Check which list is longer and loop through the longer list to find the greatest common divisor
            if len(str1_strings) > len(str2_strings):
                for string in str1_strings:
                    # Check if the string is in the other list and if the strings start with the same substring (we could also check if the strings end with the same substring)
                    if string in str2_strings and str1.startswith(string) and str2.startswith(string):
                        # Create two empty strings and append the string to the empty string as many times as it fits in the original string 
                        compare_str_1 = ""; compare_str_2 = ""
                        for i in range(int(len(str1)/len(string))): compare_str_1 += string
                        for i in range(int(len(str2)/len(string))): compare_str_2 += string
                        # Check if the strings are equal and return the string if they are
                        if compare_str_1 == str1 and compare_str_2 == str2: return string
            else:
                for string in str2_strings:
                    # Check if the string is in the other list and if the strings start with the same substring (we could also check if the strings end with the same substring)
                    if string in str1_strings and str1.startswith(string) and str2.startswith(string):
                        # Create two empty strings and append the string to the empty string as many times as it fits in the original string 
                        compare_str_1 = ""; compare_str_2 = ""
                        for i in range(int(len(str1)/len(string))): compare_str_1 += string
                        for i in range(int(len(str2)/len(string))): compare_str_2 += string
                        # Check if the strings are equal and return the string if they are
                        if compare_str_1 == str1 and compare_str_2 == str2: return string
        # Return an empty string if the input strings are not valid or if there is no greatest common divisor
        return ""

# Tests
solution = Solution()

# Test 1
str1 = "ABCABC"; str2 = "ABC"
expected = "ABC"
output = solution.gcdOfStrings(str1, str2)
assert expected == output

# Test 2
str1 = "ABABAB"; str2 = "ABAB"
expected = "AB"
output = solution.gcdOfStrings(str1, str2)
assert expected == output

# Test 3
str1 = "LEET"; str2 = "CODE"
expected = ""
output = solution.gcdOfStrings(str1, str2)
assert expected == output

# Test 4
str1 = "ABCDEF"; str2 = "ABC"
expected = ""
output = solution.gcdOfStrings(str1, str2)
assert expected == output

# Test 5
str1 = "AA"; str2 = "A"
expected = "A"
output = solution.gcdOfStrings(str1, str2)
assert expected == output

# Test 6
str1 = "ABABCCABAB"; str2 = "ABAB"
expected = ""
output = solution.gcdOfStrings(str1, str2)
assert expected == output

# Test 7
str1 = "AAAA"; str2 = "ABAB"
expected = ""
output = solution.gcdOfStrings(str1, str2)
assert expected == output

print("All tests passed")