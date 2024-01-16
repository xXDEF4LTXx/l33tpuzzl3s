# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        if len(haystack) >= 1 and len(needle) <= 10**4 and len(needle)>=1 and all(letter in list(letters) for letter in list(needle)) and all(letter in list(letters) for letter in list(haystack)):
            try: return haystack.index(needle)
            except ValueError: return -1
        return -1
solution = Solution()
