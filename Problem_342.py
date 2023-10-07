# Power of Four
"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.


"""
# solution:
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not(n & (n-1)) and int(sqrt(n)) * int(sqrt(n)) == n