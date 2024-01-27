
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

# Test cases

# Test case 1: s is a substring of itself
assert solution.repeatedSubstringPattern("abab") == True

# Test case 2: s is not a substring of itself
assert solution.repeatedSubstringPattern("aba") == False

# Test case 3: s is a substring of itself, but with a different number of copies
assert solution.repeatedSubstringPattern("abcabcabcabc") == True

# Test case 4: s is a substring of itself, but with a different number of copies
assert solution.repeatedSubstringPattern("abcabcabc") == True

# Test case 5: len(s) is 10**4
assert solution.repeatedSubstringPattern("a"*10**4) == True

# Test case 6: ababab
assert solution.repeatedSubstringPattern("ababab") == True

assert solution.repeatedSubstringPattern("abcdabcdabcdabcdabcd") == True

print('All tests passed successfully!!')