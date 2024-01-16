# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 10**4
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t) and len(s) >= 1 and len(t) <= 5 * 10**4 and all(letter in list('abcdefghijklmnopqrstuvwxyz') for letter in list(s)) and all(letter in list('abcdefghijklmnopqrstuvwxyz') for letter in list(t)) and sorted(list(s)) == sorted(list(t)): return True
        return False

solution = Solution()

# Test case 1: Anagrams
assert solution.isAnagram("anagram", "nagaram") == True

# Test case 2: Not anagrams
assert solution.isAnagram("rat", "car") == False

# Test case 3: Empty strings
assert solution.isAnagram("", "") == False

# Test case 4: Different lengths
assert solution.isAnagram("abc", "abcd") == False

# Test case 5: Non-alphabetic characters
assert solution.isAnagram("a!b", "b!a") == False

assert solution.isAnagram("aacc", "ccac") == False

print("All tests passed")