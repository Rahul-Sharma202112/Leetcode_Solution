# Count the Digits That Divide a Number
"""
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.
"""

# solution:

class Solution:
    def countDigits(self, num: int) -> int:
        count =0
        for c in str(num):
            if num % int(c)==0:
                count +=1
        return count