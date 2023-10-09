# Average Value of Even Numbers That Are Divisible by Three
"""
Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
"""

# solution

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count, sum=0,0
        for n in nums:
            if (n%2==0 and n%3==0):
                sum +=n
                count +=1
        
        if count ==0:
            return 0
        
        return sum//count