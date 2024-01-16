# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# Constraints:
# 1 <= s.length <= 10**4
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if 1 <= len(s) <= 10**4 and all(char in 'abcdefghijklmnopqrstuvwxyz ' for char in s.lower().strip()): return len(list(filter(lambda x: x!= '', list(s.strip().split(' '))))[-1])
            
        
        
solution = Solution()
s = "Hello World"
output = 5
assert solution.lengthOfLastWord(s) == output

s = "hello"
output = 5
assert solution.lengthOfLastWord(s) == output

s = "   fly me   to   the moon  "
output = 4
assert solution.lengthOfLastWord(s) == output

s = "moon  "
output = 4
assert solution.lengthOfLastWord(s) == output

s = "luffy is still joyboy"
output = 6
assert solution.lengthOfLastWord(s) == output

s = "a test a"
output = 1
assert solution.lengthOfLastWord(s) == output

s = "uPtqXtdxXsACYJOjtGNArtcvCPc    CWbfLKmlIaYQpFAYkZfltSjNjJN              hXGotGvQqyowBJgSMzoOEFQPHlA     MsbiELwZabDcGIuOlcsfVrUVxnREkgiEIzXGQiwKkBbbGLACrYYgGdNiSunIuZDCHFZvBpQIhkNTUscfOPWKwPLEKCVZDRcQGAobojPrPGhcTkeGbCODaXyGHcUXfQiYKwvifMGqFLeDUVPfdNPMaDrLcUAwnpAzDiuCSfMPWnvlDprFfinpKuyLiUNUy              IvwSPSecxcRmdwWTpuUyUngeGnE                   MJqoSSvaKThYFMOTtiIRiRCXkhq     SjpjgUqQuEcPThDjOdwogstzuQi         BpnbSHvsEcwQgrmrBugPeOtdSZG       ychzcYTJMzGJIsAFeiGXfVkZHIC            cdoAvhVnbCSmBQMRtSGbGgmEGBl kvZpjcEUMnyQcFIdYsNSrozhNoNQAHLhSAzTLUWkwGtdFapgPldNuO     jARPmJPzHeIAAensJoNzdtkqmpd   JVRwIgsASQnyAVEljpYGXftNASJlnOEktNveBbliIAPlhDEBFgkiIT         McNDtzzMfRTXNQemEeIRVawwHOp              wmqrrLGaVxQwHazcGXRTqJLaobS                  JyohRWAVyPrwOmxJXVmLMQycTlk     hiBSfOQYiQFGpMCZrVeVACLXScLALIcoRrdGDAzYYCwoFeSuARoXzAbSxXRiMHljlPmJNHerFewlDrqrPDXeyPmhxYSRbEYTqzPyBRHpdSBJnTyKZmYGSUmVTcdwmKrjwXaLamj         biywyxFhGclBVXxkefBRMqZUFnmHafaTMarCrHpvbAoAzEmBZPCZMjrTRFZaKDMmTwhanaUACHOHwkmnn  tRBONlYtbmmixijISOTruxwiUZvSrrnykhlLNNQcMitEJTwnmzIoRC   wRZkXDSJHZwSgpVpkzTNejrdtHO       NgDBGwLTDOzVWkFkMePCJYkjzKr               LcWoeabtfeoIPncVPkMzUPGfGDd gAkBXomHPeIgXlxWYpwJFHOaOAR          vTaYoKeHUDHQmXCWQRITfkZxlhhsZcVOOGZNzElYjTzrKyrZOOTztQogXvZyUmHXkHmJrOTbceszkwFFG                   QphPavmGdtUGKRCoPFibplVKbNU     izMKSANLzisuXPGbcDqSEovYaqaZEbwUXPbtQQluaubjoadJeRDczqkedbBPKsLLoswbeUwoSABIRuZTB     BnGXhFFUuxgTaxAAHLWvYeHpesfBiJhvkEWglAtqSACjfuoKkGviDlkZCnQjLEYMzstWsICqmTzrdiRhe                  XEQwwarNBdeIIQrothGhUNghLmAIFeMtepqgJgbXbqDlyIMTleCbfAzcQTmPnsvgqKkhYuSnXbnqUvwYlvYHlKWGxtKkusAixrZPiTzIuNaDXDcdhjrSovGNhkzmzAHLHbrvQzKTtHPyGopTjdRVKtdhsxWoARMdIA        jqerQEsmFodlYQtwoGjGKrMOtqG      xfiWqqEbkvATNSpawGjcGBtfyfmbMAYlUqwfVNYBApwnoxeTDxGtYeFDQFUxpPgfnAyShjUwvvYcFQjIc          mifJHNnSDbPZoWSTBbxlVJKWZYq                  HYCGXQXECCvaylaTMInWajpRhEvtJjDxAkMsirJGqbhHddkFRCOfox                fqYCsARYWOuxCYlkgzaOkRabhYw               jEnoPcPlhgUHakfZxOsIRaeKpvbparNfDEIZgVrlYuqSHscAYseOvAnWzQhUEyQCYbZMnIEDuQHxDQCsf          iqhBgubdzxzxkeNvfypCFxjtfmg      DIPruJQGKHFftRCUqBjcLQBaBGm           GilSgMRwehMQTvLmAbzsRaSnmDg               TGzxrQxamzzFKmeSKgtOgeOyjKm                 aRjHLFtSBJDTgwVtFfxMCRPzhkr       LSTiCrdNXfqgOmAGOUpLVxihRvS             wRmjzklLaIvRgwrLEncSFTeAqqBVkFEZbrFcOInylNLJYqzUtAJcNn              HPlhxNKetuZZDNsIYXBImNnDrDc             UahphttIcCmAgwLsAvesYXtYAnKStHYmlzQtMWLuhAItWpqQZWEufL     "
output = 54
assert solution.lengthOfLastWord(s) == output


print("All tests passed")