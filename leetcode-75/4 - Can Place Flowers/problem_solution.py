# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

# Constraints:
# 1 <= flowerbed.length <= 2 * 10**4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if 1 <= len(flowerbed) <= 2 * 10**4 and 0 <= n <= len(flowerbed):
            if flowerbed.count(0) == 0 and n > 1: return False
            for flowerpot in range(len(flowerbed)):
                if n == 0: break
                if flowerbed[flowerpot] == 1: continue
                if flowerpot + 1 < len(flowerbed) and flowerbed[flowerpot+1] == 0:
                    if flowerpot == 0: n-=1; flowerbed[flowerpot] = 1
                    elif flowerbed[flowerpot-1] == 0: n-=1; flowerbed[flowerpot] = 1
                    
            if n == 0: return True
            


        return False

# Tests
solution = Solution()

# Test 1
flowerbed = [1,0,0,0,1]
n = 1
expected = True
# output = solution.canPlaceFlowers(flowerbed, n)
# assert output == expected

# Test 2
flowerbed = [1,0,0,0,1]
n = 2
expected = False
output = solution.canPlaceFlowers(flowerbed, n)
assert output == expected

# Test 3
flowerbed = [0,0,1,0,1]
n = 1
expected = True
output = solution.canPlaceFlowers(flowerbed, n)
assert output == expected

# Test 4
flowerbed = [0,0,1,0,1]
n = 2
expected = False
output = solution.canPlaceFlowers(flowerbed, n)
assert output == expected

# Test 5 (large input)
flowerbed = [0,0,0,0,0,1,0,0]
n = 0
expected = True
output = solution.canPlaceFlowers(flowerbed, n)
assert output == expected

# Test 6 (large input)
flowerbed = [0,0,0,0,0,1,0,0]
n = 1
expected = True
output = solution.canPlaceFlowers(flowerbed, n)
assert output == expected

# Test 7 (massive input)
flowerbed = [0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0]
n = 3
expected = True
output = solution.canPlaceFlowers(flowerbed, n)
assert output == expected

print("All tests passed")