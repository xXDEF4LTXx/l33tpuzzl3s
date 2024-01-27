# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

# Constraints:
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Create lists of the letters in each string and an empty list for the merged string
        word_1_list = list(word1); word_2_list = list(word2); word_3_list = []
        # Make sure the strings are within the constraints and all characters in the strings are lowercase letters and not digits
        if len(word_1_list) >= 1 and len(word_2_list) <= 100 and all(letter.isalpha() and not letter.isdigit() for letter in word_1_list) and all(letter.isalpha() and not letter.isdigit() for letter in word_2_list):
            # Find the length of the longest string
            if len(word_1_list) > len(word_2_list) or len(word_1_list) == len(word_2_list): largest = len(word_1_list)
            else: largest = len(word_2_list)
            # Add the letters from the strings to the merged string in alternating order
            for x in range(0, largest):
                # Add the letter from the first string to the merged string if the index is less than the length of the first string
                if x < len(word_1_list): word_3_list.append(word_1_list[x])
                # Add the letter from the second string to the merged string if the index is less than the length of the second string
                if x < len(word_2_list): word_3_list.append(word_2_list[x])
            # Return the merged string
            return ''.join(word_3_list)

# Tests
        
solution = Solution()

word1 = "abc"
word2 = "pqr"
output = "apbqcr"
assert solution.mergeAlternately(word1, word2) == output

word1 = "ab"
word2 = "pqrs"
output = "apbqrs"
assert solution.mergeAlternately(word1, word2) == output

word1 = "abcd"
word2 = "pq"
output = "apbqcd"
assert solution.mergeAlternately(word1, word2) == output

print("All tests passed successfully")
