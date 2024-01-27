# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Example 1:
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.

# Example 2:
# Input: s = "aba"
# Output: false

# Example 3:
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 
# Constraints:
# 1 <= s.length <= 10**4
# s consists of lowercase English letters.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        letters = list('abcdefghijklmnopqrstuvwxyz')
        if len(s) >= 2 and len(s) <= 10**4 and all(letter in letters for letter in list(s)):
            if len(s)%2 == 0: s_divide = int(len(s)/2)
            else: s_divide = int(len(s)/3)
            checkstr = s[:s_divide]
            if len(s)%2 == 0: finalstr = checkstr+checkstr
            else: finalstr = checkstr+checkstr+checkstr
            if finalstr == s: return True
            checkstr = s[0:2:1]
            check = ''
            while True:
                check = check + checkstr
                if check == s: return True
                if len(check) >= len(s): break
            if len(s) > 3:
                checkstr = s[0:3:1]
                check = ''
                while True:
                    check = check + checkstr
                    if check == s: return True
                    if len(check) >= len(s): break
            return False

solution = Solution()

print(solution.repeatedSubstringPattern("abcdabcdabcdabcdabcd"))
