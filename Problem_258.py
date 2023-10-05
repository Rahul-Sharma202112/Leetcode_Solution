# Add Digits
"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


"""
# solution:

class Solution:
    def addDigits(self, num: int) -> int:
        sum =0
        while(num>9):
            while num:
                sum += num % 10 
                num = num // 10
            
            num =sum
            sum =0
        return num