# URL: https://leetcode.com/problems/merge-strings-alternately/description/
# Description: You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.
# Constraints: 1 <= word1.length, word2.length <= 100 -- word1 and word2 consist of lowercase English letters.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_1_list = list(word1)
        word_2_list = list(word2)
        word_3_list = []
        if len(word_1_list) >= 1 and len(word_2_list) <= 100 and all(letter.isalpha() and not letter.isdigit() for letter in word_1_list) and all(letter.isalpha() and not letter.isdigit() for letter in word_2_list):
            if len(word_1_list) > len(word_2_list) or len(word_1_list) == len(word_2_list): largest = len(word_1_list)
            else: largest = len(word_2_list)
            for x in range(0, largest):
                if x < len(word_1_list): word_3_list.append(word_1_list[x])
                if x < len(word_2_list): word_3_list.append(word_2_list[x])
            return ''.join(word_3_list)

# Submission Details:
# Runtime 30ms
# Beats 94.40% of users with Python3

# Memory 17.16MB
# Beats 39.88% of users with Python3